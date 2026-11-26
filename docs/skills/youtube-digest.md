# youtube-digest

## What it does

Reads a YouTube video through its transcript: it fetches captions and metadata with `yt-dlp`, cleans them with a bundled Python script, then writes a digest or study notes. It cannot see frames or hear audio, so it is text only. Body in English, description bilingual.

An AI agent cannot watch a video but can read the words. A fixed script does the repeatable part (download, clean); the agent does the reasoning. It tries the video's own language, then English, then Vietnamese. It installs nothing and calls no paid transcription service without asking. Reference points: 10 videos listed from a channel by default; 2,500 characters of description kept. Every number in this skill is a labelled reference point, not a fact about your market; the skill asks for your own figures. Trade-off: reading text only, to avoid depending on a paid service.

Source: [`packs/marketing-ecommerce/skills/youtube-digest/SKILL.md`](../../packs/marketing-ecommerce/skills/youtube-digest/SKILL.md)

## When to reach for it

The user shares a YouTube link or channel and wants a summary, notes, key points or the transcript ("tóm tắt video này", "lấy transcript", "summarize this video"). Needs `yt-dlp` and Python on the machine. The strategy-advisor pack does not include it: install it from marketing-ecommerce if you need to read videos.

## Common questions

**Why did it say there are no captions?** Some videos have none. It then offers a thin summary from title and description, or asks for another video.

**Does it install yt-dlp?** No. It tells you how and waits for your say-so.

**Can I republish the transcript?** It is for your own study or work; do not republish it.

## It's working if

- It checks that `yt-dlp` and Python work before fetching.
- The digest has a TL;DR, key points with time markers, and takeaways.
- The answer cites the video and the time markers it used.
