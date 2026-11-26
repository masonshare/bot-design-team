# watch

## What it does

Lets an AI agent watch a video: it downloads the video with `yt-dlp`, extracts auto-scaled frames with `ffmpeg`, gets a timestamped transcript (native captions first, Whisper API as a fallback), and prints frame paths for the agent to look at and combine with the transcript. This folder is third-party code by Bradley Bonanno, copied here as it is under its MIT licence (the `LICENSE` file and copyright line are kept; nothing is edited). Its text is in English.

We copy it unchanged so that it stays the author's work and stays updatable. It is heavier than `youtube-digest`: it needs `ffmpeg`, `yt-dlp` and, when a video has no captions, a Whisper API key from Groq or OpenAI (a paid service; the skill asks before any key is used and has a `--no-whisper` frames-only option). Best on videos under about 10 minutes; hard caps are 100 frames and 2 frames per second. Claude Code only: the plugin parts (`hooks/`, `commands/watch.md`, the `/watch` command and the `${CLAUDE_SKILL_DIR}` variable) work only on Claude Code. On Codex the folder is used as a plain skill: ask the agent to follow `SKILL.md` and run the scripts, installing it as the author describes. Because the folder keeps its `LICENSE`, the repo's neutral-wording check skips it. For reading only the words of a video use `youtube-digest`, which is lighter and needs no key.

Source: [`packs/marketing-ecommerce/skills/watch/SKILL.md`](../../packs/marketing-ecommerce/skills/watch/SKILL.md)

## When to reach for it

The user pastes a video link (YouTube, Vimeo, X, TikTok and other sites `yt-dlp` supports) or a local video file and asks about what is in it, including what is shown on screen. If a transcript is enough, prefer `youtube-digest`.

## Common questions

**Can it run on Codex?** As a plain skill, yes, with the manual steps; the `/watch` command, hooks and plugin install are Claude Code only.

**Does it cost money?** Captions are free. The Whisper fallback uses your own API key and is billed by that provider; skip it with `--no-whisper`.

**Why is this folder different from the others?** It is another author's code under the MIT licence, kept intact. See `docs/credits.md`.

## It's working if

- `ffmpeg` and `yt-dlp` are found before it starts, and a missing key only matters for videos without captions.
- The answer combines what the frames show with what the transcript says, with time markers.
- No key was used or paid service called without your say-so.
