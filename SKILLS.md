# SKILLS.md

RAG 变更总规范（Master Readme）

---

## 0. Purpose & Scope

本文件是本仓库的 **RAG 变更前置阅读文档**。  
任何新增或修改以下内容前，必须先阅读本文件并按流程执行：

- resume（简历原文与结构化简历）
- resource（论文、证据、原始材料）
- external links（LinkedIn/GitHub/Website/Portfolio 等）
- schema（YAML 字段、frontmatter 规范）
- retrieval 相关配置与回归集（test queries）
- 文档结构和跨文档引用

目标：保证知识库在持续更新时保持 **可检索、可追溯、可维护、一致性强**。

---

## 1. Repository Map（真实路径）

根目录：

- `SKILLS.md`：本治理规范（流程接口）
- `AGENTS.md`：执行入口约束（先读再改）
- `oliver-knowledge-base/`：主知识库目录

知识库目录：

- `oliver-knowledge-base/experiences/`：经历文档（叙事层）
- `oliver-knowledge-base/projects/`：项目文档（叙事层）
- `oliver-knowledge-base/projects/sources/`：项目原始资料（raw source）
- `oliver-knowledge-base/skills/`：技能能力文档（叙事层）
- `oliver-knowledge-base/education/`：教育文档（叙事层）
- `oliver-knowledge-base/reflections/`：反思文档（叙事层）
- `oliver-knowledge-base/structured-data/`：结构化数据（真源层）
- `oliver-knowledge-base/structured-data/raw/`：原始简历/材料提取文本
- `oliver-knowledge-base/_templates/`：模板

structured-data 依赖顺序（从上游到下游）：

1. `structured-data/raw/*.md`（或 `projects/sources/*.md`）
2. `structured-data/resume.yaml`
3. `structured-data/timeline.yaml`
4. `structured-data/skills-matrix.yaml`
5. `structured-data/projects-index.yaml`
6. `structured-data/test-queries.yaml`

---

## 2. Single Source of Truth（真源规则）

以下文件是对应领域的主真源：

- 主简历真源：`oliver-knowledge-base/structured-data/resume.yaml`
- 时间线真源：`oliver-knowledge-base/structured-data/timeline.yaml`
- 技能矩阵真源：`oliver-knowledge-base/structured-data/skills-matrix.yaml`
- 项目索引真源：`oliver-knowledge-base/structured-data/projects-index.yaml`
- 原始来源真源：
  - `oliver-knowledge-base/structured-data/raw/*.md`
  - `oliver-knowledge-base/projects/sources/*.md`

叙事文档（experiences/projects/skills/education/reflections）用于可读表达与检索增强，  
但关键事实应与结构化真源一致。

---

## 3. 变更类型与标准流程（SOP）

### A. 新增/替换 Resume

1. 写入原始文本到 `structured-data/raw/`（保留来源和日期）。
2. 更新 `structured-data/resume.yaml`（核心字段先行）。
3. 同步关联叙事文档：
   - `experiences/`、`projects/`、`skills/`、`education/`
4. 同步索引与回归：
   - `timeline.yaml`
   - `skills-matrix.yaml`
   - `test-queries.yaml`
5. 校验 Gate（见第 5 节）后再结束任务。

### B. 新增 Resource（论文、证据、资料）

1. 按类型落盘：
   - 项目论文/数据：`projects/sources/`
   - 简历或通用原始证据：`structured-data/raw/`
2. 在对应 `projects/*.md` 或 `skills/*.md`：
   - frontmatter `related` 增加引用
   - 正文增加“来源/资源”小节并建立链接
3. 如资源影响结构化事实，更新 `projects-index.yaml`、`resume.yaml` 等。
4. 将检索验证问题加入或更新 `test-queries.yaml`。

### C. 新增外链（LinkedIn/GitHub/Website/Portfolio）

1. 统一写入 `structured-data/resume.yaml > personal_info.links`。
2. 若链接与某项目强关联，再补充到 `projects-index.yaml > projects[].links`。
3. 必须保证链接可访问、协议完整（`https://`）。

### D. 任意 RAG 改动（通用）

1. 明确改动类型（A/B/C 或 schema/结构调整）。
2. 先改真源，再改叙事层。
3. 执行 Gate 1-4（第 5 节）。
4. 更新更新日期（`updated` / `last_updated`）与版本信息（如适用）。

---

## 4. 字段规范（最小必要 Schema）

### 4.1 Markdown frontmatter 必填键

所有知识文档（experience/skill/project/education/reflection/source）必须包含：

- `title`
- `type`
- `timeline`（含 `start`、`end`、`period`）
- `tags`
- `domains`
- `status`
- `importance`
- `created`
- `updated`
- `related`

### 4.2 日期格式

- 月粒度：`YYYY-MM`
- 日粒度：`YYYY-MM-DD`
- 进行中可用：`present`

### 4.3 status 枚举（按类型）

- experience：`completed | ongoing | archived`
- project：`completed | ongoing | archived`
- education：`enrolled | completed | deferred`
- reflection：`draft | completed | evergreen`
- skill：`learning | proficient | mastered | expert`
- source 文档：`archived`（建议）

说明：历史文档若已存在不同 status，可在后续维护中逐步收敛，不在一次改动中强制全量重写。

### 4.4 resume.yaml 链接字段

`personal_info.links` 统一包含以下键：

- `linkedin`
- `github`
- `website`
- `portfolio`（可选，为空字符串可接受）

---

## 5. 质量门禁（Change Gate）

任何 RAG 变更任务结束前，必须满足：

- Gate 1：路径与相对链接有效（至少核心内容目录无失效链接）
- Gate 2：结构化数据与叙事文档事实一致（公司/职位/时间/关键指标）
- Gate 3：`updated` 与 `last_updated` 已刷新（或确认同日变更）
- Gate 4：新增事实可被 `test-queries.yaml` 覆盖（新增或更新用例）

若任一 Gate 失败，不应结束任务。

---

## 6. 提交前检查清单（Checklist）

每次提交前逐项确认：

- [ ] 本次变更涉及的 resume/resource/link 是否已建立双向回链（结构化 <-> 叙事）
- [ ] `timeline.yaml` 是否新增了关键时间点
- [ ] `skills-matrix.yaml` 是否补充了新的证据与最后使用时间
- [ ] `projects-index.yaml` 是否补充了新增项目或新增资源链接
- [ ] `test-queries.yaml` 是否增加了覆盖新事实的检索回归问题
- [ ] 关键文档 `updated`/`last_updated` 是否已更新
- [ ] 链接检查是否通过（核心目录无失效相对链接）

---

## 7. 建议的最小验证命令（手工）

以下命令用于快速自检（在仓库根目录执行）：

```bash
# 1) 检查核心内容目录相对链接是否存在失效（示例脚本式检查）
while IFS= read -r f; do
  d=$(dirname "$f")
  rg -o '\]\(([^)#]+)\)' "$f" | sed -E 's/^\]\(([^)#]+)\)$/\1/' | while IFS= read -r rel; do
    case "$rel" in http*|mailto:*|'') continue;; esac
    p="$d/$rel"
    [ -e "$p" ] || echo "$f -> $rel"
  done
done < <(rg --files oliver-knowledge-base/{experiences,projects,skills,education,reflections} -g '*.md')
```

```bash
# 2) 检查 resume.yaml 中 links 是否存在
rg -n "links:|linkedin:|github:|website:|portfolio:" oliver-knowledge-base/structured-data/resume.yaml
```

```bash
# 3) 检查结构化数据更新时间字段
rg -n "last_updated|version" oliver-knowledge-base/structured-data/*.yaml
```

---

## 8. RAG 改动执行约定

- 先读本文件，再进行任何读写操作。
- 若发现本文件与仓库现实冲突：
  1. 先更新本文件（治理规则）
  2. 再执行具体数据与文档改动
- 不允许“只改叙事文档不改真源”导致事实漂移。

### Role Resume Generation Pre-Read Policy

对于任何岗位定制简历生成任务（如 `generate-role-resume`）：

1. 必须先读取根目录 `RESUME_GENERATE_SKILLS.md`。
2. 必须完成该文档定义的 preflight checklist。
3. 未打印 `pre_read=ok` 时，禁止进入生成步骤。

---

## 9. Changelog（治理规则）

- 2026-03-01：创建 `SKILLS.md`，建立 RAG 变更统一流程、真源规则、质量门禁与检查清单。
