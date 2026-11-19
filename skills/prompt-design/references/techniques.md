# Techniques worth knowing

Compact notes on third-party prompting techniques, rewritten in my own words. Read the sources for the full detail. Use a technique only when a test case shows the plain prompt falls short; each one adds length and cost.

## From The Prompt Report (Schulhoff et al., 2024)

A broad survey that sorts prompting techniques into families. Useful as a menu.

| Family | Idea | When to reach for it |
|---|---|---|
| In-context examples (few-shot) | Show the model worked input and output pairs | Output must follow a pattern or style that is hard to describe |
| Zero-shot with a cue | Give instructions plus a short framing, no examples | Simple tasks; start here |
| Thought generation (chain of thought) | Ask for reasoning steps before the answer | Math, logic, multi-factor judgement |
| Decomposition | Split a hard task into sub-tasks solved in order | Tasks that mix several jobs; this is the base of a prompt chain |
| Ensembling | Run several prompts or samples and combine the answers | A wrong answer is costly and you can afford extra calls |
| Self-criticism | The model checks or rewrites its own draft | Drafts with factual claims or strict format rules |

Points to carry over:
- Example quality beats example count. Keep examples consistent in format, varied in content, and cleanly separated into input and output.
- Example order and label balance can shift results. Shuffle examples in tests to see whether the prompt is fragile.
- Reasoning cues help on reasoning tasks and can hurt pure imitation tasks (copy this format exactly). Test both.
- Prompting results are sensitive to small wording changes; this is the reason to keep a test set and rerun it after each edit.

Variants seen in practice (named in the survey literature):
- Tree of thoughts: generate several lines of reasoning, evaluate them, continue with the best.
- Self-refine: draft, critique, rewrite, as a two-prompt loop.
- Verification chain: draft an answer, write questions that would expose errors, answer them independently, then revise.

## From Bsharat et al., "Principled Instructions Are All You Need" (2023)

The authors tested 26 hand-written principles on several model sizes and grouped them. The ones that hold up best on current models:

- Say what to do. Positive instructions steer better than lists of bans.
- Name the audience and the purpose in the prompt ("explain to a new hire", "for a legal reviewer").
- Break a complex request into a sequence of simpler ones.
- Use clear separators between instructions, examples, and input data.
- Give examples when format matters, and start the output yourself when you need a particular opening shape.
- Ask the model to say what information it lacks before it answers, instead of guessing.
- Request an answer in the natural style of a named audience or role when tone matters.
- Be explicit about the task's outcome: state the requirement, not only the topic.

Treat with caution: the paper also reports gains from tipping the model or threatening penalties. Those effects were measured on older models and are not reliable; do not build prompts on them.

## From Anthropic prompt engineering docs

Anthropic's overview lists techniques roughly in the order to try them, and recommends defining success criteria and test cases before tuning a prompt.

- Be clear and direct. Treat the model like a capable new colleague who lacks your context: give the background, the goal, and the standard.
- Use multiple examples. A few well-chosen examples fix format and tone better than extra description.
- Let the model think. Give room for step-by-step reasoning before the final answer, and keep the reasoning separate from the answer so the answer can be parsed.
- Use XML-style tags to separate parts of a prompt (instructions, documents, examples, output). Consistent tag names let you refer to a part by name.
- Give the model a role in the system prompt to set expertise and voice.
- Chain complex prompts. One subtask per call makes each step easier to check and debug.
- Long inputs: place long documents near the top and the question at the end; ask the model to quote the relevant passages before answering.
- Prefilling the start of the reply can force a format, on models and APIs that allow it.

## How these map onto this skill

| Need | Technique | Where it lands in the process |
|---|---|---|
| Fix the output shape | Few-shot example | The Gold Standard (step 2) goes into the prompt as the example |
| Reduce invented facts | Ask for missing info, verification chain | Reality Check (step 3), optional verification link in prompt-chain |
| Complex task | Decomposition | Hand over to prompt-chain |
| Several candidate ideas | Tree of thoughts | One 3-prompt cluster inside a prompt-chain |
| Strict quality | Self-refine, test set | prompt-test (feedback loop) |
| Long input | Document first, question last, tags | Draft layout (step 5) |

## Sources

- Schulhoff et al., "The Prompt Report: A Systematic Survey of Prompting Techniques" (2024): https://arxiv.org/abs/2406.06608
- Bsharat et al., "Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4" (2023): https://arxiv.org/abs/2312.16171
- Anthropic, "Prompt engineering overview": https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview
