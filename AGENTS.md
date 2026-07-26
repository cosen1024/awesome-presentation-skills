# AGENTS.md

本仓库维护一份公开、可机器校验的 Presentation Agent Skills 清单。

## 数据与文档

- `data/skills.yaml` 是已核验主清单的唯一事实源，不要直接手改 README 生成区。
- `data/candidates.yaml` 保存尚未完成核验的候选；`data/related-tools.yaml` 保存 MCP、App 和底层库。
- `data/stars.json` 是每日生成的仓库 Stars 缓存；动态数据不得写入 `data/skills.yaml`。
- `README.md` 与 `README_EN.md` 的清单区由 `scripts/render_readmes.py` 生成。
- 技术事实只采用项目自己的 GitHub README、具体 `SKILL.md`、许可证和第一方安装文档。
- 正式条目的 `source_ref`、`source_url` 和 `install_url` 必须固定到核验时的完整 commit。

## 三类主路线

1. `editable-pptx`：主要工作流生成或编辑原生 PowerPoint 对象。
2. `html-slides`：HTML/CSS/JS、Markdown、Marp、React、Vue、Reveal.js 等是权威源。
3. `image-first`：主要工作流先生成整页图片，再封装为 PPTX、PDF、Web 或视频。

导出 `.pptx` 不自动等于原生可编辑；编辑性使用独立字段描述。

## 核验边界

- `source-verified` 只表示公开仓库、具体 Skill 入口、安装说明与许可证状态已经核验。
- 它不表示已经运行 Skill、通过安全审计、验证输出质量或获得官方背书。
- 没有清晰许可证时记录 `NOASSERTION`，不要把本仓库的 MIT 许可证延伸到第三方项目。
- 自动发现只能输出候选观察结果，不得自动写入或删除 `data/skills.yaml` 条目。

## 修改与验证

修改前运行 `git status --short` 并保留已有改动。完成后运行：

```bash
python3 scripts/validate_data.py
python3 scripts/render_readmes.py --check
python3 -m unittest discover -s tests
git diff --check
```

需要重新生成 README 时运行：

```bash
python3 scripts/render_readmes.py --write
```

不要提交本地规划记录、个人 Agent 配置、凭据或与公开维护无关的机器环境信息。
