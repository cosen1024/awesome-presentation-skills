# Awesome Presentation Skills [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

[中文](README.md)

A curated list of Presentation Agent Skills for choosing editable PPTX, HTML Slides, or image-first presentation workflows by delivery format.

## Contents

<!--lint ignore awesome-list-item-->
- [Choose a route](#choose-a-route)
- [Editable PPTX](#editable-pptx)
- [HTML Slides](#html-slides)
- [Image-first Presentations](#image-first-presentations)
- [Related resources](#related-resources)
- [Contributing](#contributing)
- [License](#license)

## Choose a route

**Editable PPTX**: For formal deliverables whose text, charts, and shapes must remain editable.

**HTML Slides**: For browser-native motion, interaction, presenter tools, and frontend-grade visuals.

**Image-first Presentations**: For strong whole-slide visual consistency when image-based pages are acceptable.

> Exporting PPTX does not guarantee native editability. Stars measure repository attention, not quality; Stars on a multi-Skill repository do not represent one embedded PPT Skill.

<!--lint disable table-pipe-alignment table-cell-padding-->
<!-- CATALOG:START -->

## Editable PPTX

Workflows that directly create or edit native PowerPoint text, shapes, charts, and other objects.

| Repository / Skill | Repo Stars | Best suited for | Output and editability |
|---|---:|---|---|
| [addsumtech/slides_maker](https://github.com/addsumtech/slides_maker)<br>[slide-maker](https://github.com/addsumtech/slides_maker/blob/d1766cbf840a9f00e4c26cd08fef60a68f88bb39/skills/slide-maker/SKILL.md) | [490](https://github.com/addsumtech/slides_maker/stargazers) | Plans and builds natively editable PPTX decks from papers, code, or documents, with template matching, charts, equations, notes, and an independent review loop. | PPTX<br>Native editable |
| [anthropics/skills](https://github.com/anthropics/skills)<br>[pptx](https://github.com/anthropics/skills/blob/b29e7cf65e5cb78a5ac33d582270551bc74a14eb/skills/pptx/SKILL.md) | [172,631](https://github.com/anthropics/skills/stargazers) | Anthropic's document-skill baseline for creating, reading, editing, combining, splitting, templating, and inspecting PPTX/POTX files, notes, and comments. | PPTX<br>Native editable |
| [Binaryify/open-kimi-ppt-skill](https://github.com/Binaryify/open-kimi-ppt-skill)<br>[open-kimi-ppt](https://github.com/Binaryify/open-kimi-ppt-skill/blob/870c3e94fcd3bc3073add63c0c9fb7f3f3c5644d/skills/open-kimi-ppt/SKILL.md) | [1,596](https://github.com/Binaryify/open-kimi-ppt-skill/stargazers) | Uses a YAML-based PPTD intermediate format to create, edit, replicate, and read presentations, delivering both an editable PPTD project and a natively editable PPTX by default, with themes, element animation, local browser editing, and pre-export visual QA. | PPTD, PPTX<br>Native editable |
| [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT)<br>[cyber-ppt](https://github.com/crazyykhllc-bit/CyberPPT/blob/980e5576565f0673c67ee41b01d20ed66cb8417c/SKILL.md) | [1,661](https://github.com/crazyykhllc-bit/CyberPPT/stargazers) | Turns documents, research materials, and business data into dense consulting-style PPTX decks through evidence tables, storyline comparison, SCR, style approval, and page-by-page blueprints, while keeping the primary text and information layers editable and enforcing strict structural and visual QA. | PPTX, PNG<br>Partially editable |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)<br>[ppt-master](https://github.com/hugohe3/ppt-master/blob/de0af38a07706eee03b97f6186d8e0ffba595892/skills/ppt-master/SKILL.md) | [50,376](https://github.com/hugohe3/ppt-master/stargazers) | Generates natively editable PPTX decks from documents, URLs, and Markdown, with routed workflows for brands, layouts, template filling, and deck enhancement. | PPTX<br>Native editable |
| [jiadizhunine/deepPPT](https://github.com/jiadizhunine/deepPPT)<br>[deep-ppt](https://github.com/jiadizhunine/deepPPT/blob/3440832d6a0a72e1188d64ad7f2c15192207bc74/SKILL.md) | [25](https://github.com/jiadizhunine/deepPPT/stargazers) | Builds editable PPTX decks with PptxGenJS for Chinese or English lab meetings, defenses, journal clubs, and conferences, then applies package, layout-rule, and rendered-preview checks for deterministic and visual QA. | PPTX, PNG<br>Native editable |
| [kdnsna/ultimate-ppt-master-skill](https://github.com/kdnsna/ultimate-ppt-master-skill)<br>[ultimate-ppt-master](https://github.com/kdnsna/ultimate-ppt-master-skill/blob/1749ad4587e78972493b1978816092210215072a/SKILL.md) | [2](https://github.com/kdnsna/ultimate-ppt-master-skill/stargazers) | Turns PDFs, Word files, URLs, Markdown, or existing PPTX decks into local presentation projects that deliver editable PPTX, magazine-style web decks, or both, with previews and quality gates. | PPTX, HTML<br>Native editable |
| [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills)<br>[pptx-generator](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/skills/pptx-generator/SKILL.md) | [13,477](https://github.com/MiniMax-AI/skills/stargazers) | Creates presentations with PptxGenJS, edits existing PPTX files through XML workflows, and extracts content with MarkItDown. | PPTX<br>Native editable |
| [ningzimu/image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill)<br>[image-to-editable-ppt](https://github.com/ningzimu/image-to-editable-ppt-skill/blob/dfc461b05982ab5b3605c3bb2626a7d54ee80155/skills/image-to-editable-ppt/SKILL.md) | [2,244](https://github.com/ningzimu/image-to-editable-ppt-skill/stargazers) | Reconstructs images, scanned PDFs, and image-based PPTX decks into object-level editable PowerPoint slides with native text, simple shapes, separate visual assets, and notes. | PPTX<br>Native editable |
| [Noi1r/powerpoint-skill](https://github.com/Noi1r/powerpoint-skill)<br>[powerpoint-slides](https://github.com/Noi1r/powerpoint-skill/blob/a39cd8cfba332741a96d52bebd2bb378b638364e/powerpoint-slides/SKILL.md) | [115](https://github.com/Noi1r/powerpoint-skill/stargazers) | Builds PPTX decks from papers, research notes, and technical content, emphasizing native equations, multiple diagram pipelines, academic structure, and visual QA. | PPTX<br>Native editable |
| [tristan-mcinnis/pptx-from-layouts-skill](https://github.com/tristan-mcinnis/pptx-from-layouts-skill)<br>[pptx-from-layouts](https://github.com/tristan-mcinnis/pptx-from-layouts-skill/blob/53b0e750694d807e3510c2017744197c3c5089b0/.claude/skills/pptx-from-layouts/SKILL.md) | [25](https://github.com/tristan-mcinnis/pptx-from-layouts-skill/stargazers) | Maps Markdown outlines onto a corporate template's real Slide Master layouts and placeholders, with template profiling, semantic layout selection, surgical editing, and validation. | PPTX<br>Native editable |

## HTML Slides

Workflows whose authoritative presentation source is HTML, CSS, JavaScript, Markdown, or frontend components.

| Repository / Skill | Repo Stars | Best suited for | Output and editability |
|---|---:|---|---|
| [1weiho/open-slide](https://github.com/1weiho/open-slide)<br>[create-slide](https://github.com/1weiho/open-slide/blob/c408ba031154306b571b3c70d0373b77d65807a4/packages/core/skills/create-slide/SKILL.md) | [7,305](https://github.com/1weiho/open-slide/stargazers) | Authors presentations as React page components inside an open-slide workspace, with themes, feedback markers, stepped reveals, transitions, and live editing. | HTML, PDF<br>Source editable |
| [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)<br>[huashu-design](https://github.com/alchaincyf/huashu-design/blob/3b1d873575c17e6b350b4887c8416860a11ffd30/SKILL.md) | [23,708](https://github.com/alchaincyf/huashu-design/stargazers) | Uses HTML for high-fidelity slides, prototypes, motion, and visualization, with a mandatory three-direction design gate before production, review, and export. | HTML, PPTX, MP4, GIF<br>Source editable |
| [bluedusk/html-slides](https://github.com/bluedusk/html-slides)<br>[html-slides](https://github.com/bluedusk/html-slides/blob/d8289f4c317905cc5d0ca265d32b791e6cb387b7/SKILL.md) | [76](https://github.com/bluedusk/html-slides/stargazers) | Generates zero-build, single-file HTML decks with structured Pro components and creative Vibe themes, plus PPTX or HTML conversion, speaker notes, and in-browser editing. | HTML, PDF<br>Source editable |
| [codesstar/next-slide](https://github.com/codesstar/next-slide)<br>[next-slide](https://github.com/codesstar/next-slide/blob/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/SKILL.md) | [50](https://github.com/codesstar/next-slide/stargazers) | Creates zero-dependency HTML presentations or converts PPT content from natural-language requests, with curated styles, bilingual support, and scenario scaffolds. | HTML<br>Source editable |
| [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill)<br>[html-ppt](https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/SKILL.md) | [8,131](https://github.com/lewislulu/html-ppt-skill/stargazers) | Produces static HTML decks from themes, full-deck templates, page layouts, CSS/Canvas animations, speaker scripts, timers, and presenter mode. | HTML, PNG<br>Source editable |
| [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)<br>[guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill/blob/929c2ecb63a22b54d400c4911ed70bf96c2b355d/SKILL.md) | [25,263](https://github.com/op7418/guizang-ppt-skill/stargazers) | Generates horizontal-swipe single-file HTML decks with editorial-magazine and Swiss International styles, templates, motion, and a presentation runtime. | HTML<br>Source editable |
| [ryanbbrown/revealjs-skill](https://github.com/ryanbbrown/revealjs-skill)<br>[revealjs](https://github.com/ryanbbrown/revealjs-skill/blob/d0ccd344c4aaf9f045e5a15be6a2ab67b595796f/skills/revealjs/SKILL.md) | [400](https://github.com/ryanbbrown/revealjs-skill/stargazers) | Creates no-build Reveal.js HTML decks with themes, multi-column layouts, code highlighting, Chart.js, speaker notes, animation, overflow checks, in-browser text editing, and PDF export. | HTML, PDF<br>Source editable |
| [sunbigfly/ppt-agent-skills](https://github.com/sunbigfly/ppt-agent-skills)<br>[ppt-agent](https://github.com/sunbigfly/ppt-agent-skills/blob/13e353776d0ba774eff7c423cc3e529cfe0adbeb/SKILL.md) | [888](https://github.com/sunbigfly/ppt-agent-skills/stargazers) | Uses a state machine and multi-agent workflow for intake, research or source synthesis, narrative outlining, style locking, per-slide HTML production, and visual QA before exporting PNG- or SVG-based PPTX decks. | HTML, PNG, PPTX<br>Partially editable |
| [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides)<br>[frontend-slides](https://github.com/zarazhangrui/frontend-slides/blob/9906a34d640d2111f724544cbc50f7f130569ae1/SKILL.md) | [28,404](https://github.com/zarazhangrui/frontend-slides/stargazers) | Creates zero-dependency, animation-rich single-file HTML presentations, converts PowerPoint content to web slides, and uses visual previews for style selection. | HTML, PDF<br>Source editable |
| [zl190/md-slides](https://github.com/zl190/md-slides)<br>[md-slides](https://github.com/zl190/md-slides/blob/e5d3f55f3e94cc1c28e6a6cd3a75af219c5a0086/.claude/skills/md-slides/SKILL.md) | [7](https://github.com/zl190/md-slides/stargazers) | Uses Markdown as a shared source and selects Marp, Pandoc, Beamer, python-pptx, or Reveal.js to produce PDF, PPTX, and HTML presentations. | HTML, PDF, PPTX<br>Source editable |

## Image-first Presentations

Workflows that generate whole-slide images before packaging them as PPTX, PDF, web, or video outputs.

| Repository / Skill | Repo Stars | Best suited for | Output and editability |
|---|---:|---|---|
| [JuneYaooo/gpt-image2-ppt-skills](https://github.com/JuneYaooo/gpt-image2-ppt-skills)<br>[gpt-image2-ppt](https://github.com/JuneYaooo/gpt-image2-ppt-skills/blob/64643a7fb4365bb21191bdcead1d767d0bbd9c27/SKILL.md) | [1,218](https://github.com/JuneYaooo/gpt-image2-ppt-skills/stargazers) | Uses gpt-image-2 to generate high-resolution slide images from bundled styles or a user PPTX template, packages them as a 16:9 deck, and offers an editable reconstruction route. | PNG, PPTX<br>Image-based |
| [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill)<br>[codex-ppt](https://github.com/ningzimu/codex-ppt-skill/blob/7e5437fe0edeaede717c506eb08ad1ee45cbf30f/skills/codex-ppt/SKILL.md) | [5,379](https://github.com/ningzimu/codex-ppt-skill/stargazers) | Plans outlines and visual styles from articles, reports, papers, and course notes, generates whole-slide images, and assembles them into PPTX with a local script. | PNG, PPTX<br>Image-based |
| [NyxTides/ppt-image-first](https://github.com/NyxTides/ppt-image-first)<br>[ppt-image-first](https://github.com/NyxTides/ppt-image-first/blob/87a300a559a2a55097fab337241218c6557bfa23/SKILL.md) | [1,198](https://github.com/NyxTides/ppt-image-first/stargazers) | Uses intake, content, style-preview, and specification gates to turn a vague topic into an image-first deck plan, whole-slide visuals, and a final presentation. | PNG, PPTX<br>Image-based |
| [op7418/NanoBanana-PPT-Skills](https://github.com/op7418/NanoBanana-PPT-Skills)<br>[ppt-generator-pro](https://github.com/op7418/NanoBanana-PPT-Skills/blob/0c18b9abde04ad42f4f62c7e9ead346b7bb39260/SKILL.md) | [3,226](https://github.com/op7418/NanoBanana-PPT-Skills/stargazers) | Generates whole-slide PPT images with Nano Banana and can add page transitions, an interactive player, and a complete presentation video. | PNG, PPTX, VIDEO<br>Image-based |

<!-- CATALOG:END -->
<!--lint enable table-pipe-alignment table-cell-padding-->

## Related resources

[Related Tools](docs/related-tools.md) covers MCP servers, templates, and underlying libraries. [Methodology](docs/methodology.md) explains scope, classification, and inclusion criteria.

## Contributing

New Skills and corrections are welcome. Read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request.

## License

Catalog data and documentation use [CC0 1.0 Universal](LICENSE). Automation scripts and workflows use the [MIT License](LICENSE-CODE). Third-party projects retain their own licenses.
