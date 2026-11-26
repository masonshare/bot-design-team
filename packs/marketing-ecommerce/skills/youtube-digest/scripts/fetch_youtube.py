#!/usr/bin/env python3
"""Fetch a YouTube video's metadata + auto-caption transcript via yt-dlp,
clean it, and write a digest-input markdown file. Prints the output path.

Usage:
  python fetch_youtube.py <youtube_url> [output_dir] [lang]
  python fetch_youtube.py list <channel_url> [N]
  lang is optional (for example "vi" or "fr.*"). Without it the script tries the
  video's own language, then en, then vi.
Needs yt-dlp on PATH. Works on Windows, macOS and Linux.
"""
import sys
import os
import re
import glob
import json
import subprocess

# Force UTF-8 stdout so Vietnamese / non-ASCII titles print on Windows (cp1252) consoles
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def run(args):
    return subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")


def list_channel(url, n):
    """Print the most recent N videos of a channel/playlist as 'url<TAB>title'."""
    if "/videos" not in url and "list=" not in url and ("@" in url or "/channel/" in url or "/c/" in url or "/user/" in url):
        url = url.rstrip("/") + "/videos"
    res = run(["yt-dlp", "--flat-playlist", "--no-warnings", "--playlist-end", str(n),
               "--print", "%(url)s\t%(title)s", url])
    if res.returncode != 0:
        print("ERROR listing channel:\n" + (res.stderr or "")[-1000:])
        sys.exit(2)
    print(res.stdout.strip())


def clean_vtt(path):
    """VTT -> plain text, dropping cue timestamps, tags, and rolling duplicates."""
    with open(path, encoding="utf-8", errors="replace") as f:
        raw = f.read().splitlines()
    out = []
    prev = None
    for ln in raw:
        if "-->" in ln:
            continue
        s = ln.strip()
        if not s or s.startswith("WEBVTT") or s.startswith("Kind:") or s.startswith("Language:"):
            continue
        if s.isdigit():  # cue index
            continue
        s = re.sub(r"<[^>]+>", "", s).strip()  # strip inline <c> / timestamp tags
        s = re.sub(r"\[[^\]]*\]", "", s)  # strip [Music] etc.
        s = s.replace(" ", " ").replace("&nbsp;", " ")  # non-breaking spaces
        s = re.sub(r"&[a-z]+;", " ", s)  # other html entities (&amp; &gt; ...)
        s = re.sub(r"\s+", " ", s).strip()  # collapse whitespace
        if not s or s == prev:
            continue
        out.append(s)
        prev = s
    return "\n".join(out)


def main():
    if len(sys.argv) < 2:
        print("usage:\n"
              "  python fetch_youtube.py <video_url> [output_dir] [lang_glob]\n"
              "  python fetch_youtube.py list <channel_url> [N]   # list recent videos")
        sys.exit(1)
    if sys.argv[1] == "list":
        if len(sys.argv) < 3:
            print("usage: python fetch_youtube.py list <channel_url> [N]")
            sys.exit(1)
        n = int(sys.argv[3]) if len(sys.argv) > 3 else 10
        list_channel(sys.argv[2], n)
        return
    url = sys.argv[1]
    outdir = sys.argv[2] if len(sys.argv) > 2 else "."
    lang = sys.argv[3] if len(sys.argv) > 3 else None  # explicit override; else auto try-order
    os.makedirs(outdir, exist_ok=True)

    meta = run(["yt-dlp", "--skip-download", "--no-warnings", "--dump-single-json", url])
    if meta.returncode != 0:
        print("ERROR fetching metadata:\n" + (meta.stderr or "")[-1000:])
        sys.exit(2)
    j = json.loads(meta.stdout)
    vid = j.get("id", "video")
    title = j.get("title", "") or ""
    uploader = j.get("uploader", "") or j.get("channel", "") or ""
    dur = j.get("duration_string") or str(j.get("duration", "") or "")
    desc = (j.get("description") or "")[:2500]
    chapters = j.get("chapters") or []

    # Try one language at a time (combined wildcard globs are unreliable in some yt-dlp builds).
    # Prefer the video's own language, then English, then Vietnamese, then *-orig variants.
    vid_lang = (j.get("language") or "").strip()
    try_langs = []
    for x in [lang, vid_lang, "en", "vi", "en-US", "en-orig", "vi-orig"]:
        if x and x not in try_langs:
            try_langs.append(x)
    transcript = ""
    used_lang = None
    vtts = []
    for lg in try_langs:
        run(["yt-dlp", "--skip-download", "--no-warnings", "--write-auto-subs", "--write-subs",
             "--sub-langs", lg, "--sub-format", "vtt",
             "-o", os.path.join(outdir, "%(id)s.%(ext)s"), url])
        vtts = sorted(glob.glob(os.path.join(outdir, vid + "*.vtt")))
        if vtts:
            transcript = clean_vtt(vtts[0])
            used_lang = lg
            break

    out = os.path.join(outdir, vid + "_digest-input.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n")
        f.write(f"- uploader: {uploader}\n- duration: {dur}\n- url: {url}\n- video_id: {vid}\n")
        f.write(f"- caption_lang: {used_lang or 'none'}\n\n")
        if chapters:
            f.write("## Chapters\n")
            for c in chapters:
                f.write(f"- {int(c.get('start_time', 0))}s — {c.get('title', '')}\n")
            f.write("\n")
        f.write("## Description\n" + desc + "\n\n")
        f.write("## Transcript\n")
        f.write(transcript if transcript else "(no auto-subtitles available)\n")

    # tidy: remove raw vtt files
    for v in vtts:
        try:
            os.remove(v)
        except OSError:
            pass
    print(out)


if __name__ == "__main__":
    main()
