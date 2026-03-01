# RAG 系统设置指南

本指南帮助你将 Oliver Knowledge Base 接入 RAG（检索增强生成）系统，实现智能问答和信息检索。

## 🎯 系统目标

构建一个能够准确回答以下问题的 RAG 系统：
- "Oliver在哪里工作过？"
- "Oliver会用Python做什么？"
- "Oliver大学期间做过什么项目？"
- "Oliver的机器学习经验如何？"
- "Oliver在2022年做了什么？"

## 📊 架构选择

### 推荐架构：混合检索 + 重排序

```
用户查询
    ↓
[元数据过滤] ← 使用 frontmatter 的 tags, timeline
    ↓
[双路检索]
    ├─ 向量检索（语义相似度）
    └─ 关键词检索（BM25）
    ↓
[结果融合] ← 使用 Reciprocal Rank Fusion
    ↓
[重排序] ← 使用专门的 reranker 模型
    ↓
[上下文构建] ← 组装 Top-K 结果
    ↓
[LLM 生成答案]
```

## 🛠️ 技术栈建议

### 选项 1：LangChain + Vector DB（推荐新手）
```python
# 技术栈
- LangChain: 0.1.x
- Vector DB: Pinecone / Weaviate / Chroma
- Embedding: OpenAI text-embedding-3-large
- LLM: GPT-4 / Claude 3.5
- Metadata 过滤: 原生支持

# 优点：快速上手，生态完善
# 缺点：较重，自定义困难
```

### 选项 2：LlamaIndex（推荐文档检索）
```python
# 技术栈
- LlamaIndex: 0.10.x
- Vector Store: 多种选择
- Embedding: BGE-M3 (中英混合)
- LLM: 灵活选择
- Router: 智能路由到不同索引

# 优点：专为文档设计，强大的索引能力
# 缺点：学习曲线略陡
```

### 选项 3：自建系统（推荐高级用户）
```python
# 技术栈
- Vector DB: Qdrant / Milvus
- Embedding: 自托管模型（如 BGE-M3）
- BM25: Elasticsearch / 自实现
- Reranker: bge-reranker-large
- LLM: 本地 Ollama 或 API

# 优点：完全控制，性能优化空间大
# 缺点：开发成本高
```

## 📝 文档预处理

### 1. Frontmatter 解析
```python
import yaml
import re

def parse_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取 frontmatter
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if match:
        metadata = yaml.safe_load(match.group(1))
        body = match.group(2)
        return metadata, body
    return {}, content
```

### 2. 分块策略

#### 策略 A：基于 Markdown 标题
```python
# 推荐：保持语义完整性
- 按 ## 标题分块
- 每块包含标题内容
- 块大小：300-500 tokens
- 重叠：50 tokens
```

#### 策略 B：固定大小
```python
# 简单但可能切断语义
- 固定 400 tokens
- 重叠 100 tokens
```

#### 策略 C：语义分块（最佳）
```python
# 使用 LlamaIndex 的 SemanticSplitter
from llama_index.core.node_parser import SemanticSplitterNodeParser

splitter = SemanticSplitterNodeParser(
    buffer_size=1,
    breakpoint_percentile_threshold=95
)
```

### 3. 元数据索引

为每个 chunk 添加丰富的元数据：
```python
chunk_metadata = {
    "source_file": "experiences/google-swe.md",
    "title": "Software Engineer @ Google",
    "type": "experience",
    "timeline_start": "2023-06",
    "timeline_end": "present",
    "timeline_period": "grad_and_career",
    "tags": ["Python", "Backend", "Cloud"],
    "domains": ["technology", "software-engineering"],
    "importance": 5,
    "section": "Core Projects",  # 所在章节
    "has_code": False,
    "word_count": 342
}
```

## 🔍 检索策略

### 1. 元数据预过滤
```python
# 时间范围查询
filter = {
    "timeline_start": {"$gte": "2020-01"},
    "timeline_end": {"$lte": "2023-12"}
}

# 类型过滤
filter = {
    "type": {"$in": ["project", "experience"]}
}

# 标签匹配
filter = {
    "tags": {"$contains": "Machine-Learning"}
}
```

### 2. 向量检索配置
```python
# Embedding 模型选择
models = {
    "英文为主": "text-embedding-3-large (OpenAI)",
    "中英混合": "bge-m3 (BAAI)",
    "本地部署": "gte-large-zh (Alibaba)"
}

# 检索参数
top_k = 10  # 初始召回
similarity_threshold = 0.7  # 相似度阈值
```

### 3. 混合检索
```python
from langchain.retrievers import EnsembleRetriever

# 向量检索器
vector_retriever = vectorstore.as_retriever(
    search_kwargs={"k": 10}
)

# BM25 关键词检索器
bm25_retriever = BM25Retriever.from_documents(documents)
bm25_retriever.k = 10

# 混合（权重可调）
ensemble_retriever = EnsembleRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    weights=[0.6, 0.4]  # 语义 60%, 关键词 40%
)
```

### 4. 重排序
```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# 使用 Cross-Encoder 重排序
model = AutoModelForSequenceClassification.from_pretrained(
    'BAAI/bge-reranker-large'
)

def rerank(query, documents, top_n=5):
    pairs = [[query, doc.page_content] for doc in documents]
    scores = model.predict(pairs)
    
    # 按分数排序，取 top_n
    ranked_docs = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )[:top_n]
    
    return [doc for doc, score in ranked_docs]
```

## 💬 提示词工程

### System Prompt 示例
```
你是 Oliver 的个人知识助手。你的任务是基于提供的文档准确回答关于 Oliver 的问题。

知识库包含：
- 工作经历和项目经验
- 技能和专业知识
- 教育背景
- 个人反思和想法

回答要求：
1. 仅基于提供的文档回答，不要编造信息
2. 如果信息不在文档中，明确说明"我没有找到相关信息"
3. 引用具体的文档和时间点
4. 量化信息时使用文档中的具体数字
5. 对于技能问题，参考熟练度评级（beginner/intermediate/advanced/expert）

文档格式说明：
- experiences/: 工作和实习经历
- projects/: 具体项目详情
- skills/: 技能掌握情况
- education/: 教育背景
- reflections/: 个人思考

回答格式：
- 简洁明了，突出关键信息
- 包含时间线（如适用）
- 引用来源文档
```

### Query 优化
```python
def optimize_query(user_query):
    """扩展用户查询，提升召回"""
    
    # 时间识别
    if "现在" in user_query or "目前" in user_query:
        user_query += " timeline_end:present"
    
    # 同义词扩展
    synonyms = {
        "工作": ["experience", "job", "position"],
        "项目": ["project", "work"],
        "技能": ["skill", "expertise", "proficiency"]
    }
    
    # 实体识别（公司、技术等）
    # 可使用 NER 模型
    
    return expanded_query
```

## 📈 评估与优化

### 1. 构建测试集
创建 `test-queries.yaml`：
```yaml
test_cases:
  - query: "Oliver在Google工作时做了什么？"
    expected_docs: ["experiences/google-swe.md"]
    expected_info: ["Backend development", "Python", "2023-present"]
  
  - query: "Oliver的机器学习水平如何？"
    expected_docs: ["skills/machine-learning.md"]
    expected_info: ["advanced", "TensorFlow", "multiple projects"]
  
  - query: "Oliver大学时期的主要项目"
    expected_docs: ["projects/thesis.md", "projects/undergrad-research.md"]
    filters: {"timeline_period": "college"}
```

### 2. 评估指标
```python
# 检索质量
- Recall@K: 相关文档的召回率
- MRR (Mean Reciprocal Rank): 首个相关结果的位置
- NDCG: 考虑排序质量的指标

# 生成质量
- Faithfulness: 答案与文档的一致性
- Answer Relevance: 答案与问题的相关性
- Context Precision: 检索上下文的精确度
```

### 3. 优化方向

**如果召回率低**：
- 增加 top_k
- 降低相似度阈值
- 调整 embedding 模型
- 改进 query 扩展

**如果精确度低**：
- 加强重排序
- 优化元数据过滤
- 改进 chunk 策略
- 提升 prompt 质量

**如果答案不准确**：
- 检查文档质量
- 优化 system prompt
- 使用更强的 LLM
- 增加引用要求

## 🚀 快速开始示例

### 使用 LangChain 的最小实现
```python
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# 1. 加载文档
loader = DirectoryLoader(
    "oliver-knowledge-base",
    glob="**/*.md",
    exclude=["_templates", "**/README.md"]
)
documents = loader.load()

# 2. 分块
splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "Header 1"),
        ("##", "Header 2"),
    ]
)
splits = splitter.split_documents(documents)

# 3. 创建向量库
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# 4. 创建 RAG chain
llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(
        search_kwargs={"k": 5}
    ),
    return_source_documents=True
)

# 5. 查询
result = qa_chain("Oliver的Python水平如何？")
print(result["result"])
print("来源：", [doc.metadata["source"] for doc in result["source_documents"]])
```

## 🔧 高级功能

### 1. 多索引路由
```python
# 为不同类型的文档创建专门索引
indices = {
    "experiences": create_index("experiences/"),
    "projects": create_index("projects/"),
    "skills": create_index("skills/"),
}

# 根据查询类型路由
def route_query(query):
    if "工作" in query or "公司" in query:
        return indices["experiences"]
    elif "项目" in query:
        return indices["projects"]
    # ...
```

### 2. 时间线查询
```python
# 实现时间范围过滤
def query_timeline(start_date, end_date):
    filter = {
        "timeline_start": {"$gte": start_date},
        "timeline_end": {"$lte": end_date}
    }
    return vectorstore.similarity_search(query, filter=filter)
```

### 3. 关系图谱
```python
# 构建实体关系
relationships = {
    "projects": {
        "project-1": {
            "used_skills": ["Python", "TensorFlow"],
            "part_of_experience": "google-swe",
            "timeline": "2023-06"
        }
    }
}

# 增强检索：找到相关实体
```

## 📚 推荐资源

### 学习资料
- [LangChain Documentation](https://python.langchain.com/)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [RAG 最佳实践](https://www.pinecone.io/learn/retrieval-augmented-generation/)

### 工具与服务
- **向量数据库**：Pinecone, Weaviate, Qdrant, Chroma
- **Embedding 服务**：OpenAI, Cohere, HuggingFace
- **评估框架**：RAGAS, TruLens

---

**下一步**：选择一个技术栈，开始实现你的 Oliver RAG 系统！





