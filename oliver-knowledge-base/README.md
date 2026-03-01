# Oliver Knowledge Base

> ⚠️ 变更入口规则：任何 RAG 相关修改前，请先阅读仓库根目录的 [`SKILLS.md`](../SKILLS.md)。

## 🎯 架构设计理念

这是一个专为 **RAG（检索增强生成）** 优化的个人知识库，采用单一维度+元数据的扁平化结构，确保高效检索和准确召回。

## 📁 文件夹结构

```
oliver-knowledge-base/
├── experiences/       # 工作经历、实习、志愿者等所有经历
├── skills/           # 技能和专业知识领域
├── projects/         # 项目详细描述
├── education/        # 教育背景、课程、证书
├── reflections/      # 个人反思、思考、学习笔记
└── structured-data/  # 结构化数据（JSON/YAML格式的简历、时间线等）
```

## 🏷️ 元数据标准

每个 Markdown 文件都应包含统一的 frontmatter 元数据：

```yaml
---
title: "文档标题"
type: "experience|skill|project|education|reflection"
timeline: 
  start: "2020-03"
  end: "2022-06"
  period: "college"  # childhood|highschool|college|grad_and_career
tags: ["AI", "Python", "Research", "Machine-Learning"]
domains: ["technology", "finance", "research"]
status: "completed|ongoing|archived"
importance: 5  # 1-5 重要性评分
created: 2025-10-19
updated: 2025-10-19
related: ["project-xyz.md", "skill-python.md"]  # 相关文档链接
---
```

## 📝 文档编写最佳实践

### 1. 开头总结
每个文档开头应有 2-3 句话的摘要，便于 RAG 快速理解内容：

```markdown
## 摘要
这是关于XXX项目的详细记录，主要涉及机器学习模型开发和部署。该项目在2020-2022年完成，使用Python和TensorFlow实现。
```

### 2. 结构化内容
使用清晰的标题层级和列表：

```markdown
## 技术栈
- Python 3.8+
- TensorFlow 2.x
- Docker

## 主要成果
1. 提升模型准确率15%
2. 减少推理时间50%
```

### 3. 关键词密度
确保重要概念和技术名词多次出现，提升检索准确率。

### 4. 时间信息
明确标注时间点和持续时长，便于时间线检索。

## 🔍 RAG 优化建议

### Chunk 大小
- 推荐：300-500 tokens
- 使用 Markdown 标题作为自然分割点

### 检索策略
1. **混合检索**：语义检索 + 关键词检索
2. **元数据过滤**：先用 tags/timeline 过滤，再进行向量检索
3. **重排序**：使用 importance 字段和时间新近度重排

### Embedding 模型
- 推荐：OpenAI text-embedding-3-large 或 BGE-M3（中英混合）
- 维度：1024-1536

## 📊 标签分类体系

### 技能类标签
`Python`, `JavaScript`, `Machine-Learning`, `Deep-Learning`, `Data-Analysis`, `Frontend`, `Backend`, `DevOps`, `Cloud`, `Database`

### 领域类标签
`Finance`, `Healthcare`, `Education`, `Research`, `Business`, `Product`, `Design`

### 活动类标签
`Work`, `Internship`, `Project`, `Research`, `Volunteer`, `Competition`, `Course`

### 时期标签
`childhood`, `highschool`, `college`, `grad_and_career`

## 🔗 交叉引用

使用相对链接在文档间建立联系：

```markdown
相关项目：[Resume Builder](../projects/resume-builder.md)
使用技能：[Python开发](../skills/python.md)
```

## 🚀 快速开始

1. 选择合适的文件夹创建新文档
2. 复制 `_templates/` 中的模板
3. 填写完整的 frontmatter
4. 添加摘要和结构化内容
5. 标注相关文档链接
6. 若涉及 resume/resource/link 或检索逻辑改动，按 [`SKILLS.md`](../SKILLS.md) 的 SOP 与 Gate 完成校验

---

*最后更新：2025-10-19*
