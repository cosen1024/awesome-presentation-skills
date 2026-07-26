# 收录与核验方法

## 收录边界

主清单收录公开 GitHub 仓库中能够定位到具体 `SKILL.md` 的 Presentation Agent Skill。普通 AI PPT App、MCP、模板集合和 PPTX 库不进入主清单，但可以作为 Related Tools。

## 三类判定

- `editable-pptx`：主要流程通过 PptxGenJS、python-pptx、Office XML、PowerPoint API 等创建或编辑原生对象。
- `html-slides`：HTML/CSS/JS、Markdown、Marp、React、Vue、Reveal.js 等源文件是权威演示源。
- `image-first`：主要流程生成整页图片，再封装为 PPTX、PDF、网页或视频。

分类依据是主要创作表示，不是最终导出扩展名。每个条目只有一个主分类；转换、模板、动画、学术等能力通过标签记录。

## 第一手核验

正式条目必须检查：

1. 公开 GitHub 仓库；
2. 精确的 `SKILL.md`；
3. 第一方 README 或安装文档；
4. 仓库级或 Skill 级许可证，或明确记录其缺失；
5. 第一方说明的平台、依赖和外部 API 限制；
6. 核验时的完整 commit SHA。

搜索结果、文章、截图、社交帖子和 stars 只能作为发现线索，不能单独支持正式收录。

## 状态语义

- `source-verified`：源码、具体入口、安装说明与许可证状态已核验。
- `not-tested`：没有代表本目录执行过该 Skill。
- `not-reviewed`：没有代表本目录完成安全或权限审查。

目录不会把源代码可见性描述为运行成功、安全、输出高质量或官方背书。

## 自动发现

`config/discovery.yaml` 保存版本化查询。`scripts/discover_github.py` 输出候选观察 JSON，只包含公开仓库元数据和发现来源；它没有写入 `data/skills.yaml` 的代码路径。候选晋级始终由人工完成。

## 动态信号

stars、最近 push、归档状态和默认分支属于动态健康信息，不进入固定核验事实，也不作为收录硬门槛。仓库 Stars 单独保存在生成缓存 `data/stars.json` 中，每天通过 GitHub REST API 刷新后重新生成中英文 README；网络错误会保留上次成功值，不自动删除条目。
