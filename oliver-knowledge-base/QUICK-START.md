# 🚀 快速开始指南

欢迎使用 Oliver Knowledge Base！这是一个为 RAG 优化的个人知识库系统。

## 📂 文件夹结构

```
oliver-knowledge-base/
├── experiences/       # 工作、实习、志愿者等所有经历
├── skills/           # 技能和专业知识
├── projects/         # 项目详细信息
├── education/        # 教育背景和课程
├── reflections/      # 个人反思和学习笔记
├── structured-data/  # YAML/JSON 格式的结构化数据
└── _templates/       # 各类文档的模板
```

## ⚡ 5分钟快速开始

### 1️⃣ 创建第一个文档

**步骤：**
1. 选择合适的文件夹（如 `experiences/`）
2. 复制对应的模板文件
3. 填写 frontmatter 元数据
4. 编写内容

**示例：创建一个工作经历**

```bash
# 复制模板
cp _templates/experience-template.md experiences/my-first-job.md

# 用编辑器打开并填写
code experiences/my-first-job.md
```

填写关键信息：
- ✅ 完整的 frontmatter（title, timeline, tags, domains）
- ✅ 2-3句话的摘要
- ✅ 结构化的职责和成果
- ✅ 量化的数据（如"提升性能20%"）

### 2️⃣ 建立文档关联

在文档中使用相对链接建立关系：

```markdown
## 使用的技能
- [Python](../skills/python.md)
- [React](../skills/react.md)

## 完成的项目
- [项目A](../projects/project-a.md)
```

### 3️⃣ 维护结构化数据

定期更新 `structured-data/resume.yaml`，保持与 Markdown 文档同步：

```yaml
experience:
  - title: "Software Engineer"
    company: "Company Name"
    start_date: "2023-06"
    markdown_link: "../experiences/my-first-job.md"
```

## 📝 文档编写最佳实践

### ✅ DO（推荐做法）

1. **完整的元数据**
   ```yaml
   ---
   title: "清晰的标题"
   type: "experience"
   timeline:
     start: "2023-06"
     end: "present"
   tags: ["Python", "Backend", "AWS"]
   importance: 5
   ---
   ```

2. **开头摘要**
   ```markdown
   ## 摘要
   简洁描述这个经历/项目/技能的核心内容。2-3句话即可。
   ```

3. **量化成果**
   - ✅ "提升系统性能35%"
   - ✅ "管理团队5人"
   - ✅ "服务10万+用户"

4. **建立链接**
   - 链接到相关项目
   - 链接到使用的技能
   - 链接到相关经历

5. **使用标签**
   - 技术标签：`Python`, `React`, `AWS`
   - 领域标签：`Finance`, `Healthcare`, `Research`
   - 活动标签：`Work`, `Internship`, `Project`

### ❌ DON'T（避免的做法）

1. ❌ 缺少 frontmatter 元数据
2. ❌ 过于简短，缺少细节
3. ❌ 没有时间信息
4. ❌ 缺少上下文和背景
5. ❌ 没有链接到相关文档

## 🏷️ 标签体系

### 技能类标签
`Python`, `JavaScript`, `React`, `TensorFlow`, `AWS`, `Docker`, `Git`, `SQL`

### 领域类标签
`AI`, `Web-Development`, `Data-Science`, `Finance`, `Healthcare`, `Research`

### 时期标签
`childhood`, `highschool`, `college`, `grad_and_career`

### 状态标签
- **status**: `completed`, `ongoing`, `archived`
- **proficiency**: `beginner`, `intermediate`, `advanced`, `expert`

## 📊 文件命名规范

### Experiences（经历）
```
{company-name}-{position}.md

示例:
- google-software-engineer.md
- meta-swe-intern-2022.md
```

### Projects（项目）
```
{project-name-in-kebab-case}.md

示例:
- ai-resume-optimizer.md
- real-time-chat-app.md
```

### Skills（技能）
```
{skill-name-in-kebab-case}.md

示例:
- python.md
- machine-learning.md
- react-development.md
```

### Education（教育）
```
{institution-abbreviation}-{degree}-{major}.md

示例:
- mit-bs-computer-science.md
- stanford-ms-ai.md
```

### Reflections（反思）
```
{topic-in-kebab-case}.md
或
{date}-{topic}.md

示例:
- learning-ml-journey.md
- 2024-q4-career-reflection.md
```

## 🔗 内部链接语法

使用相对路径链接到其他文档：

```markdown
# 从 experiences/ 链接到 projects/
[项目名称](../projects/project-name.md)

# 从 projects/ 链接到 skills/
[Python](../skills/python.md)

# 从任何地方链接到 structured-data/
[简历数据](../structured-data/resume.yaml)
```

## 📋 日常工作流程

### 每周维护
1. 更新正在进行的项目
2. 添加新学到的技能
3. 记录重要的工作成果

### 每月维护
1. 写一篇月度反思
2. 更新 `structured-data/resume.yaml`
3. 审查和改进现有文档

### 重要事件后
1. 完成新项目 → 创建项目文档
2. 换工作 → 完成工作经历文档
3. 掌握新技能 → 创建或更新技能文档
4. 获得认证 → 更新教育/技能文档

## 🎯 内容优先级

建议按以下顺序填充知识库：

### 第一阶段：核心经历（1-2天）
1. ✅ 最近的工作经历（最近2-3份工作）
2. ✅ 核心技能（5-10个最重要的技能）
3. ✅ 代表性项目（3-5个最佳项目）
4. ✅ 最高学历教育背景

### 第二阶段：完整历史（1周）
5. ✅ 所有工作和实习经历
6. ✅ 完整的技能清单
7. ✅ 所有值得展示的项目
8. ✅ 完整教育背景

### 第三阶段：深度内容（持续）
9. ✅ 项目的技术深度细节
10. ✅ 技能的学习历程
11. ✅ 个人反思和思考
12. ✅ 结构化数据完善

## 💡 实用技巧

### 1. 使用 VS Code 插件
- **Markdown All in One**：快速编辑 Markdown
- **YAML**：验证 frontmatter 语法
- **Markdown Links**：管理文档间链接

### 2. 创建别名（Bash/Zsh）
```bash
# 添加到 ~/.zshrc 或 ~/.bashrc
alias kb="cd '/Users/pppop/Desktop/Oliver RAG/oliver-knowledge-base'"
alias kbe="code '/Users/pppop/Desktop/Oliver RAG/oliver-knowledge-base'"
```

### 3. 模板快速访问
在编辑器中为模板创建代码片段。

### 4. Git 版本控制
```bash
cd oliver-knowledge-base
git init
git add .
git commit -m "Initial knowledge base"

# 定期提交
git add .
git commit -m "Update: 新增项目X"
```

### 5. 搜索技巧
```bash
# 搜索所有提到 "Python" 的文档
grep -r "Python" . --include="*.md"

# 搜索特定标签
grep -r "tags:.*Machine-Learning" . --include="*.md"

# 搜索时间段
grep -r "2023-" . --include="*.md"
```

## 🔍 RAG 集成

准备好填充内容后，参考以下文档设置 RAG 系统：

1. 📖 阅读 [RAG-SETUP-GUIDE.md](./RAG-SETUP-GUIDE.md)
2. 🛠️ 选择技术栈（LangChain / LlamaIndex / 自建）
3. 🚀 实现基础检索功能
4. 📈 评估和优化

## 📚 完整文档

- [README.md](./README.md) - 完整的架构说明和最佳实践
- [RAG-SETUP-GUIDE.md](./RAG-SETUP-GUIDE.md) - 详细的 RAG 系统设置
- [_templates/](./templates/) - 各类文档模板
- 各文件夹的 README.md - 具体类型文档的说明

## ❓ 常见问题

### Q: 一个项目同时属于某个工作经历，应该放在哪里？
A: 在 `projects/` 创建详细的项目文档，在 `experiences/` 的工作文档中链接过去。

### Q: 技能文档应该多详细？
A: 至少包括：熟练度、学习历程、应用项目、相关技能。高级的可以加代码示例。

### Q: 需要多久更新一次？
A: 有重要变化时立即更新（如完成项目、换工作）。常规内容每周或每月更新。

### Q: 私密信息怎么处理？
A: 使用 `.gitignore` 排除敏感文件，或使用 `-private` 后缀标记私密文档。

### Q: 如何保持结构化数据和 Markdown 同步？
A: 建议以 Markdown 为主，结构化数据作为索引。或编写脚本自动生成。

---

**下一步**：选择一个模板，开始创建你的第一个文档！🎉

有问题？查看 [README.md](./README.md) 或相应文件夹的 README。





