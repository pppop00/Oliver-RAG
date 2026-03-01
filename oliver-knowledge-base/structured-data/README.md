# 结构化数据 (Structured Data)

这个文件夹存放 JSON 或 YAML 格式的结构化数据，便于程序化处理和快速检索。

## 内容类型
- ✅ **简历数据**：多版本的简历数据（YAML/JSON）
- ✅ **时间线**：完整的人生时间线
- ✅ **技能矩阵**：技能清单和熟练度
- ✅ **项目列表**：所有项目的索引
- ✅ **联系人网络**：重要的导师、同事、合作者
- ✅ **成绩单**：学术成绩的数字化记录
- ✅ **证书清单**：所有认证和证书

## 文件格式
推荐使用 YAML（更易读）或 JSON（更通用）：
```
resume.yaml
timeline.yaml
skills-matrix.json
projects-index.yaml
certifications.json
```

## 当前已维护文件（Oliver）
- `resume.yaml`：主简历结构化数据（教育/经历/技能/论文）
- `timeline.yaml`：时间线事件索引
- `skills-matrix.yaml`：技能矩阵（熟练度+证据）
- `projects-index.yaml`：研究项目索引
- `test-queries.yaml`：RAG 检索回归测试集

## 使用模板
参考 `../_templates/structured-data-resume.yaml` 了解数据结构。

## 主要文件说明

### resume.yaml
包含完整的简历信息，可以：
- 生成不同格式的简历（LaTeX, HTML, PDF）
- 快速更新和维护
- 程序化筛选和定制内容

### timeline.yaml
个人完整时间线：
```yaml
timeline:
  - date: "2019-09"
    event: "Started undergraduate at University X"
    category: "education"
    importance: 5
    link: "../education/university-x.md"
  
  - date: "2020-06"
    event: "First internship at Company Y"
    category: "experience"
    importance: 4
    link: "../experiences/company-y-intern.md"
```

### skills-matrix.yaml
技能清单和评级：
```yaml
skills:
  programming:
    - name: "Python"
      proficiency: "expert"
      years: 5
      last_used: "2025-10"
      link: "../skills/python.md"
```

### contacts.yaml
重要人际网络（⚠️ 注意隐私）：
```yaml
contacts:
  - name: "Professor Jane Doe"
    relationship: "PhD Advisor"
    institution: "University X"
    field: "Machine Learning"
    connection_date: "2020-09"
    notes: "Thesis advisor, expertise in deep learning"
```

## 数据一致性
⚠️ **重要**：结构化数据应与 Markdown 文档保持同步
- 定期审查和更新
- 使用 `last_updated` 字段追踪更新时间
- 考虑编写脚本自动验证一致性

## RAG 应用
结构化数据的优势：
1. **快速筛选**：按时间、标签、类型筛选
2. **精确查询**：结构化查询（如"2022年的所有项目"）
3. **关系映射**：可视化技能-项目-经历的关系
4. **元数据索引**：为 Markdown 文档提供索引

## 岗位简历生成流程约束
当执行岗位定制简历生成（`generate-role-resume`）时，流程依赖根目录
`RESUME_GENERATE_SKILLS.md`。该文档定义了：
- 技能优先级规则
- 1-page 裁剪策略
- 生成前 preflight checklist

⚠️ `resume-output/` 目录中的生成文件是产物，不是结构化真源。  
禁止反向覆盖 `resume.yaml`、`timeline.yaml`、`skills-matrix.yaml`。

## 数据导出
可以基于这些数据生成：
- 📄 PDF 简历
- 🌐 个人网站
- 📊 技能可视化图表
- 📅 交互式时间线
- 🔗 知识图谱

## 隐私与安全
⚠️ 此文件夹可能包含敏感信息：
- 考虑加密存储
- 不要提交到公开仓库
- 在 `.gitignore` 中排除敏感文件
- 使用环境变量或密钥管理

## 推荐工具
- **YAML 编辑器**：VS Code + YAML 插件
- **JSON 验证**：[jsonlint.com](https://jsonlint.com)
- **数据转换**：`yq`, `jq` 命令行工具
- **简历生成**：JSONResume, HackMyResume



