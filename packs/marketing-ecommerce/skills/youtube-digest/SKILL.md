---
name: youtube-digest
description: Read a YouTube video through its transcript - fetches captions and metadata with yt-dlp, cleans them, then writes a structured digest or study notes. Use when the user shares a YouTube link or channel and wants a summary, notes, key points, or the transcript ("tóm tắt video này", "đọc video YouTube này", "lấy transcript", "summarize this video"). Works on public videos with captions; needs yt-dlp and Python on the machine; does not watch frames or listen to audio.
---

# youtube-digest

An AI agent cannot watch a video but can read its transcript. This skill pulls the captions and metadata with `yt-dlp`, cleans them into plain text, and turns that into what the user asked for.

## Before you start (check once)

- `yt-dlp --version` must work. If not, tell the user it is missing and give the install line for their system (for example `pip install yt-dlp`, or the package manager they use). Do not install without their say-so.
- `python --version` must work (the cleaner is a Python script). On some systems the command is `python3`.
- No API key is needed. Internet is required. Only public videos with captions (automatic or manual) work.

Paths below use `<skill-dir>` for the folder that holds this SKILL.md.

## Workflow

1. **Get the URL** of one video. For a playlist or channel, ask which video, or process the latest N only if the user insists. Do not dump a whole channel.
2. **Optional: list a channel's latest videos** so the user can choose:
   ```bash
   python "<skill-dir>/scripts/fetch_youtube.py" list "<CHANNEL_URL>" 10
   ```
   It prints `url<TAB>title` for the latest N videos.
3. **Fetch the transcript** into a folder the user agrees to (default: a `youtube-notes` folder in the current project):
   ```bash
   python "<skill-dir>/scripts/fetch_youtube.py" "<VIDEO_URL>" "<output_dir>"
   ```
   It prints the path of `<video-id>_digest-input.md`, which holds metadata, chapters, description, and the clean transcript. The script tries the video's own language first, then English, then Vietnamese; pass a language code as a third argument to force one. The language used is recorded in the file header as `caption_lang`.
4. **Read** that file.
5. **Produce what the user asked for.** Default is a digest:
   - **TL;DR**: 3 to 5 bullets.
   - **Key points**, with chapter or time markers when chapters exist.
   - **Actionable takeaways**.
   - If the video teaches a topic, add concepts taught and questions worth testing yourself on.
6. **Cite the source**: video URL, title, channel, and the time markers you relied on.
7. **Save** only if the user wants it. Offer a note file or a Google Doc if connected; never overwrite an existing file.

## Edge cases

- **No captions**: the file says `(no auto-subtitles available)` and `caption_lang: none`. Tell the user. Offer to summarise from title, description, and chapters only (and say that is thin), or suggest a video that has captions. Do not buy or call a transcription service without asking.
- **Age-restricted or private video**: yt-dlp errors. Report it. Do not try to bypass.
- **Very long video**: summarise section by section, using chapters.
- **Playlist or channel link**: confirm the scope first.
- **Other languages**: handled by the language try-order. Write the digest in the language the user is using unless they ask otherwise.

## Limits

- Automatic captions contain mistakes and repeats. The cleaner removes rolling duplicates, but treat exact wording as approximate, and do not quote it as a verbatim statement.
- This skill reads text only. It cannot see slides, charts, or demos. If the answer depends on what is shown on screen, say so.
- Summarising a video is for the user's own study or work. Do not republish a transcript or long extracts of it.
