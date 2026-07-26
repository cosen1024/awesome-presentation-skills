# Contributing

感谢帮助维护 Awesome Presentation Skills。本项目优先保证证据清晰，不追求无差别收录。

## 主清单准入条件

- 与演示文稿创建、编辑、转换、重建或质量检查直接相关。
- 能定位到公开 GitHub 仓库中的具体 `SKILL.md`。
- 有第一方 README、安装入口或明确的使用入口。
- 记录许可证；没有清晰许可证时使用 `NOASSERTION` 并说明。
- 用一个完整 commit 固定 `source_url` 和 `install_url`。
- 描述客观、简短，不使用“最好、革命性、魔法、最强”等营销词。

stars 不是准入条件，也不是质量评分。

## 分类规则

- 原生创建或编辑 PowerPoint 对象：`editable-pptx`
- HTML/前端代码是权威源：`html-slides`
- 整页图片是主要内容层：`image-first`

最终能导出 PPTX 不决定分类。

## 提交步骤

1. 在 `data/skills.yaml` 中新增或修改条目。
2. 不要直接修改 README 的生成区。
3. 运行：

```bash
python3 scripts/validate_data.py
python3 scripts/render_readmes.py --write
python3 scripts/render_readmes.py --check
python3 -m unittest discover -s tests
git diff --check
npx --yes awesome-lint@2.1.2
```

4. PR 说明应包含仓库、具体 Skill、主分类、输入输出、许可证、安装入口和维护信号。

一个 PR 尽量只新增、移除或修正一个 Skill，避免夹带无关排序和文案修改。

更多数据结构、自动发现、Stars 缓存和定时任务说明见 [维护指南](docs/maintenance.md)。
