# Awesome Presentation Skills [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

[English](README_EN.md)

精选的 Presentation Agent Skills 清单，帮助你按交付形式选择可编辑 PPTX、HTML 演示或图片式 PPT 工作流。

## 目录

<!--lint ignore awesome-list-item-->
- [如何选择](#如何选择)
- [可编辑 PPTX](#可编辑-pptx)
- [HTML 演示](#html-演示)
- [图片式 PPT](#图片式-ppt)
- [相关资源](#相关资源)
- [贡献](#贡献)
- [许可](#许可)

## 如何选择

**可编辑 PPTX**：适合需要继续修改文字、图表和形状的正式交付。

**HTML 演示**：适合强调动画、交互、演讲者模式和前端视觉表现的场景。

**图片式 PPT**：适合优先追求整页视觉效果，并能接受页面主体为图片的场景。

> “导出 PPTX”不等于“原生可编辑”。Stars 是仓库级关注度，不是质量评分；多 Skill 仓库的 Stars 也不代表单个 PPT Skill。

<!--lint disable table-pipe-alignment table-cell-padding-->
<!-- CATALOG:START -->

## 可编辑 PPTX

主要工作流直接创建或编辑 PowerPoint 原生文本、形状、图表和其他对象。

| 仓库 / Skill | 仓库 Stars | 适合做什么 | 输出与编辑性 |
|---|---:|---|---|
| [addsumtech/slides_maker](https://github.com/addsumtech/slides_maker)<br>[slide-maker](https://github.com/addsumtech/slides_maker/blob/d1766cbf840a9f00e4c26cd08fef60a68f88bb39/skills/slide-maker/SKILL.md) | [293](https://github.com/addsumtech/slides_maker/stargazers) | 从论文、代码或文档规划并生成原生可编辑 PPTX，包含模板适配、图表公式、讲稿和独立评审闭环。 | PPTX<br>原生可编辑 |
| [anthropics/skills](https://github.com/anthropics/skills)<br>[pptx](https://github.com/anthropics/skills/blob/b29e7cf65e5cb78a5ac33d582270551bc74a14eb/skills/pptx/SKILL.md) | [164,210](https://github.com/anthropics/skills/stargazers) | 面向 PPTX/POTX 的创建、读取、编辑、合并、拆分、模板处理、讲稿和评论操作，是 Claude 官方文档 Skill 基线。 | PPTX<br>原生可编辑 |
| [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT)<br>[cyber-ppt](https://github.com/crazyykhllc-bit/CyberPPT/blob/980e5576565f0673c67ee41b01d20ed66cb8417c/SKILL.md) | [1,445](https://github.com/crazyykhllc-bit/CyberPPT/stargazers) | 将文档、研究材料和业务数据经过证据表、故事线比较、SCR、风格确认与逐页蓝图，制作成主要文字和信息层可编辑的高密度咨询式 PPTX，并执行严格的结构与视觉 QA。 | PPTX, PNG<br>部分可编辑 |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)<br>[ppt-master](https://github.com/hugohe3/ppt-master/blob/de0af38a07706eee03b97f6186d8e0ffba595892/skills/ppt-master/SKILL.md) | [41,125](https://github.com/hugohe3/ppt-master/stargazers) | 从文档、URL 和 Markdown 生成原生可编辑 PPTX，并支持品牌、布局、模板填充和现有演示增强路线。 | PPTX<br>原生可编辑 |
| [kdnsna/ultimate-ppt-master-skill](https://github.com/kdnsna/ultimate-ppt-master-skill)<br>[ultimate-ppt-master](https://github.com/kdnsna/ultimate-ppt-master-skill/blob/1749ad4587e78972493b1978816092210215072a/SKILL.md) | [146](https://github.com/kdnsna/ultimate-ppt-master-skill/stargazers) | 从 PDF、Word、URL、Markdown 或既有 PPTX 建立本地演示项目，按交付场景生成可编辑 PPTX、杂志风网页演示或双交付，并包含预览与质量门禁。 | PPTX, HTML<br>原生可编辑 |
| [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills)<br>[pptx-generator](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/skills/pptx-generator/SKILL.md) | [13,164](https://github.com/MiniMax-AI/skills/stargazers) | 使用 PptxGenJS 创建演示、通过 XML 工作流编辑现有 PPTX，并用 MarkItDown 提取内容。 | PPTX<br>原生可编辑 |
| [ningzimu/image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill)<br>[image-to-editable-ppt](https://github.com/ningzimu/image-to-editable-ppt-skill/blob/dfc461b05982ab5b3605c3bb2626a7d54ee80155/skills/image-to-editable-ppt/SKILL.md) | [1,600](https://github.com/ningzimu/image-to-editable-ppt-skill/stargazers) | 把图片、扫描 PDF 和图片版 PPTX 分解并重建为对象级可编辑 PowerPoint，恢复文本、简单形状、独立视觉资产和页面备注。 | PPTX<br>原生可编辑 |
| [Noi1r/powerpoint-skill](https://github.com/Noi1r/powerpoint-skill)<br>[powerpoint-slides](https://github.com/Noi1r/powerpoint-skill/blob/a39cd8cfba332741a96d52bebd2bb378b638364e/powerpoint-slides/SKILL.md) | [102](https://github.com/Noi1r/powerpoint-skill/stargazers) | 为论文、研究笔记和技术内容生成 PPTX，重点支持原生公式、多种图示管线、学术结构与视觉 QA。 | PPTX<br>原生可编辑 |
| [tristan-mcinnis/pptx-from-layouts-skill](https://github.com/tristan-mcinnis/pptx-from-layouts-skill)<br>[pptx-from-layouts](https://github.com/tristan-mcinnis/pptx-from-layouts-skill/blob/53b0e750694d807e3510c2017744197c3c5089b0/.claude/skills/pptx-from-layouts/SKILL.md) | [8](https://github.com/tristan-mcinnis/pptx-from-layouts-skill/stargazers) | 将 Markdown 大纲映射到企业模板真实的 Slide Master 布局和占位符，支持模板画像、语义布局选择、局部编辑与结果校验。 | PPTX<br>原生可编辑 |

## HTML 演示

以 HTML、CSS、JavaScript、Markdown 或前端组件作为权威演示源。

| 仓库 / Skill | 仓库 Stars | 适合做什么 | 输出与编辑性 |
|---|---:|---|---|
| [1weiho/open-slide](https://github.com/1weiho/open-slide)<br>[create-slide](https://github.com/1weiho/open-slide/blob/c408ba031154306b571b3c70d0373b77d65807a4/packages/core/skills/create-slide/SKILL.md) | [5,990](https://github.com/1weiho/open-slide/stargazers) | 在 open-slide 工作区中把每套演示写成 React 页面组件，并配合主题、反馈标记、逐步揭示、转场和实时编辑。 | HTML, PDF<br>源文件可编辑 |
| [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)<br>[huashu-design](https://github.com/alchaincyf/huashu-design/blob/3b1d873575c17e6b350b4887c8416860a11ffd30/SKILL.md) | [22,018](https://github.com/alchaincyf/huashu-design/stargazers) | 用 HTML 完成高保真幻灯片、原型、动画和可视化，要求先输出三个真实设计方向，再进入制作、评审和导出流程。 | HTML, PPTX, MP4, GIF<br>源文件可编辑 |
| [bluedusk/html-slides](https://github.com/bluedusk/html-slides)<br>[html-slides](https://github.com/bluedusk/html-slides/blob/d8289f4c317905cc5d0ca265d32b791e6cb387b7/SKILL.md) | [69](https://github.com/bluedusk/html-slides/stargazers) | 生成单文件、零构建依赖的 HTML 演示，提供结构化 Pro 组件和创意 Vibe 主题，并支持 PPTX 或现有 HTML 转换、讲稿和浏览器内编辑。 | HTML, PDF<br>源文件可编辑 |
| [codesstar/next-slide](https://github.com/codesstar/next-slide)<br>[next-slide](https://github.com/codesstar/next-slide/blob/e92c1b2506e6cf5acff7d2b92339ba0c0ce2af22/SKILL.md) | [43](https://github.com/codesstar/next-slide/stargazers) | 用自然语言创建零依赖 HTML 演示或转换 PPT 内容，提供多种风格、双语支持和场景脚手架。 | HTML<br>源文件可编辑 |
| [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill)<br>[html-ppt](https://github.com/lewislulu/html-ppt-skill/blob/f3a8435d3901697d5ac5e64d356c933637e43107/SKILL.md) | [7,389](https://github.com/lewislulu/html-ppt-skill/stargazers) | 以主题、整套模板、页面布局、CSS/Canvas 动画、讲稿、计时器和演讲者模式批量组织静态 HTML 幻灯片。 | HTML, PNG<br>源文件可编辑 |
| [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)<br>[guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill/blob/929c2ecb63a22b54d400c4911ed70bf96c2b355d/SKILL.md) | [22,381](https://github.com/op7418/guizang-ppt-skill/stargazers) | 生成横向翻页的单文件 HTML 演示，主打电子杂志与瑞士国际主义风格，并包含模板、动效和演示运行时。 | HTML<br>源文件可编辑 |
| [ryanbbrown/revealjs-skill](https://github.com/ryanbbrown/revealjs-skill)<br>[revealjs](https://github.com/ryanbbrown/revealjs-skill/blob/d0ccd344c4aaf9f045e5a15be6a2ab67b595796f/skills/revealjs/SKILL.md) | [377](https://github.com/ryanbbrown/revealjs-skill/stargazers) | 生成无需构建即可打开的 Reveal.js HTML 演示，支持主题、多栏布局、代码高亮、Chart.js、讲稿、动画、溢出检查、浏览器内文本编辑和 PDF 导出。 | HTML, PDF<br>源文件可编辑 |
| [sunbigfly/ppt-agent-skills](https://github.com/sunbigfly/ppt-agent-skills)<br>[ppt-agent](https://github.com/sunbigfly/ppt-agent-skills/blob/13e353776d0ba774eff7c423cc3e529cfe0adbeb/SKILL.md) | [862](https://github.com/sunbigfly/ppt-agent-skills/stargazers) | 以状态机和多 Agent 流程完成采访、检索或资料整理、叙事大纲、风格锁定、逐页 HTML 生成与视觉 QA，并导出 PNG 或 SVG 路线的 PPTX。 | HTML, PNG, PPTX<br>部分可编辑 |
| [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides)<br>[frontend-slides](https://github.com/zarazhangrui/frontend-slides/blob/9906a34d640d2111f724544cbc50f7f130569ae1/SKILL.md) | [26,352](https://github.com/zarazhangrui/frontend-slides/stargazers) | 创建零依赖、动画丰富的单文件 HTML 演示，也能把 PowerPoint 内容转换为网页幻灯片，并通过视觉预览帮助选择风格。 | HTML, PDF<br>源文件可编辑 |
| [zl190/md-slides](https://github.com/zl190/md-slides)<br>[md-slides](https://github.com/zl190/md-slides/blob/e5d3f55f3e94cc1c28e6a6cd3a75af219c5a0086/.claude/skills/md-slides/SKILL.md) | [7](https://github.com/zl190/md-slides/stargazers) | 以 Markdown 为统一源文件，根据场景选择 Marp、Pandoc、Beamer、python-pptx 或 Reveal.js，生成 PDF、PPTX 和 HTML 演示。 | HTML, PDF, PPTX<br>源文件可编辑 |

## 图片式 PPT

先生成整页幻灯片图片，再封装为 PPTX、PDF、网页或视频。

| 仓库 / Skill | 仓库 Stars | 适合做什么 | 输出与编辑性 |
|---|---:|---|---|
| [JuneYaooo/gpt-image2-ppt-skills](https://github.com/JuneYaooo/gpt-image2-ppt-skills)<br>[gpt-image2-ppt](https://github.com/JuneYaooo/gpt-image2-ppt-skills/blob/64643a7fb4365bb21191bdcead1d767d0bbd9c27/SKILL.md) | [1,105](https://github.com/JuneYaooo/gpt-image2-ppt-skills/stargazers) | 用 gpt-image-2 按内置风格或用户 PPTX 模板逐页生成高清图片，再封装为 16:9 PPTX，并提供可编辑重建路线。 | PNG, PPTX<br>图片式 |
| [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill)<br>[codex-ppt](https://github.com/ningzimu/codex-ppt-skill/blob/7e5437fe0edeaede717c506eb08ad1ee45cbf30f/skills/codex-ppt/SKILL.md) | [4,146](https://github.com/ningzimu/codex-ppt-skill/stargazers) | 从文章、报告、论文和课程笔记规划大纲与视觉风格，生成整页图片并用本地脚本组装成 PPTX。 | PNG, PPTX<br>图片式 |
| [NyxTides/ppt-image-first](https://github.com/NyxTides/ppt-image-first)<br>[ppt-image-first](https://github.com/NyxTides/ppt-image-first/blob/87a300a559a2a55097fab337241218c6557bfa23/SKILL.md) | [1,171](https://github.com/NyxTides/ppt-image-first/stargazers) | 通过需求、内容、风格预览和规格锁定等确认关卡，把模糊主题转成图片式演示计划、整页视觉和最终 PPT。 | PNG, PPTX<br>图片式 |
| [op7418/NanoBanana-PPT-Skills](https://github.com/op7418/NanoBanana-PPT-Skills)<br>[ppt-generator-pro](https://github.com/op7418/NanoBanana-PPT-Skills/blob/0c18b9abde04ad42f4f62c7e9ead346b7bb39260/SKILL.md) | [3,161](https://github.com/op7418/NanoBanana-PPT-Skills/stargazers) | 使用 Nano Banana 生成整页 PPT 图片，并可进一步生成页面转场、交互播放器和完整演示视频。 | PNG, PPTX, VIDEO<br>图片式 |

<!-- CATALOG:END -->
<!--lint enable table-pipe-alignment table-cell-padding-->

## 相关资源

[相关工具](docs/related-tools.md) 收录 MCP、模板和底层库；[收录与核验方法](docs/methodology.md) 说明分类和准入标准。

## 贡献

欢迎提交新的 Skill 或修正现有信息。请先阅读[贡献指南](CONTRIBUTING.md)。

## 许可

清单数据与文档采用 [CC0 1.0 Universal](LICENSE)；自动化脚本与工作流采用 [MIT License](LICENSE-CODE)。第三方项目仍遵循各自的许可证。
