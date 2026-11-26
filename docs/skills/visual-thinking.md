# visual-thinking

## What it does

Turns an analysis, strategy or framework into a diagram on demand: strategy canvas (value curve), customer journey map, 2x2 matrix, system and feedback-loop diagram, one-page business canvas, funnel, radar, positioning map. It only draws what an analysis already says; to analyse a journey or find conversion leaks use `journey-mapper` first. It maps framework to diagram to tool, with a decision tree for choosing Mermaid text, plain SVG or an HTML page. Body in Vietnamese, description bilingual. Two ready HTML templates (a value-curve chart in inline SVG and a CSS-grid canvas) live in `references/html-chart-canvas.md`.

Analysis defaults to words, but some results are understood much faster when seen. The default for non-technical users is a private HTML page or a new slide, falling back to Mermaid or a text table in the reply. The HTML templates depend on no library; a chart library from a CDN is used only if the user agrees, and the skill names no address. Making the result look polished through an image or design tool is an optional step that always asks first when it costs credits. Reference points: about 8 nodes per diagram (12 for a flowchart); 5 to 8 factors and 2 to 3 lines on a strategy canvas; radar with at most 3 options and 5 to 8 criteria; at most 3 bullets per canvas cell; journey map scale 1 to 5. Every number in this skill is a labelled reference point, not a fact about your market; the skill asks for your own figures. Trade-off: the self-built SVG default loses interactivity, so the page runs offline and loads no outside code. Both HTML templates were opened in a browser during import; one chart fix is described in the PR.

Source: [`packs/strategy-advisor/skills/visual-thinking/SKILL.md`](../../packs/strategy-advisor/skills/visual-thinking/SKILL.md)

## When to reach for it

Someone asks to draw or visualise a strategy canvas, a journey, a 2x2, a feedback loop, a one-page canvas, a funnel, a radar or a positioning map. Several pack skills point here for diagrams (`stp-marketing-strategy`, `market-researcher`, `journey-mapper`); those links are soft, and each has a table fallback.

## Common questions

**Will the diagram open for someone who is not technical?** The default is a private HTML page or a slide. Mermaid may not render in every viewer, so the skill also gives a text table.

**Does it load code from the internet?** No, unless you agree to a chart library. The default templates work offline.

**Does it invent data?** No. It only draws what the analysis said, and example data in the templates is made up and labelled.

## It's working if

- The diagram type and tool were chosen from the mapping table and the viewer, with the reason.
- The chart or canvas opens and renders correctly, with axes, units and assumed numbers labelled.
- Three reading lines sit under the diagram: what it shows, what stands out, what follows.
