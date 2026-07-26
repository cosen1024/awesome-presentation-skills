# 维护指南

本页面向仓库维护者；普通使用者只需阅读项目首页和各上游 Skill 的安装说明。

## 数据与生成

- `data/skills.yaml` 是已核验主清单的事实源。
- `data/stars.json` 是生成的仓库 Stars 缓存。
- `data/candidates.yaml` 保存尚未完成核验的候选。
- `data/related-tools.yaml` 保存 MCP、模板和底层库。
- `README.md` 与 `README_EN.md` 的分类清单由 `scripts/render_readmes.py` 生成。

不要直接修改 README 的 `CATALOG` 标记区。

## 本地验证

```bash
python3 scripts/validate_data.py
python3 scripts/render_readmes.py --write
python3 scripts/render_readmes.py --check
python3 -m unittest discover -s tests
git diff --check
npx --yes awesome-lint@2.1.2
```

## 自动维护

- `validate.yml` 在 push 和 pull request 时验证数据、生成结果与测试。
- `discover.yml` 定时搜索候选项目，只生成候选报告，不直接修改正式清单。
- `health.yml` 定时检查固定证据链接。
- `stars.yml` 每日更新仓库 Stars；数值没有变化时不创建提交。

自动发现结果必须经过人工检查第一方 `SKILL.md`、安装说明、许可证和固定 commit 后，才能进入正式清单。

## 动态信息

Stars 属于仓库级动态信号，不是单个 Skill 的质量分数。固定核验事实与动态缓存分开维护，网络失败时保留上次成功值。

## 发布前检查

1. 中英文 README 同步生成。
2. 所有新增条目具有完整 commit SHA 和固定链接。
3. 许可证缺失时使用 `NOASSERTION` 并提供双语说明。
4. 本地验证和 GitHub Actions 均通过。
5. 不提交个人路径、凭据、本地 Agent 配置或规划记录。
