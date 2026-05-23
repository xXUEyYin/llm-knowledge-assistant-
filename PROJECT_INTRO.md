# 🧠 LLM Knowledge Assistant

## 项目概述

LLM Knowledge Assistant 是一个基于 **RAG（Retrieval-Augmented Generation，检索增强生成）** 架构的智能企业知识助手。该项目旨在帮助企业快速构建基于自身文档资料的智能问答系统，让用户能够通过自然语言的方式高效地查询和获取企业知识。

## 🎯 核心功能

### 1. PDF 文档知识库
- 支持上传 PDF 格式的企业文档
- 自动解析和提取文档文本内容
- 将文档内容切分为可管理的知识块

### 2. 语义向量检索
- 使用 SentenceTransformer 将文本转换为高维向量
- 基于 FAISS 向量数据库实现高效的相似度检索
- 支持自然语言查询，返回最相关的知识内容

### 3. LLM 智能问答
- 集成 OpenAI 兼容 API（默认使用 DeepSeek）
- 基于检索到的上下文生成准确答案
- 支持上下文感知的问题回答

### 4. 多入口交互
- **Web 界面**：基于 Streamlit 的可视化交互界面
- **命令行界面**：轻量级的命令行问答工具
- 支持工具调用功能扩展（如天气查询）

## 🏗 技术架构

### 系统流程

```
用户问题
   ↓
语义向量化（SentenceTransformer）
   ↓
向量检索（FAISS）
   ↓
获取相关文档片段
   ↓
构建增强 Prompt
   ↓
大语言模型生成（DeepSeek API）
   ↓
返回答案
```

### 核心技术组件

| 组件 | 技术选型 | 说明 |
|------|----------|------|
| 文本向量化 | SentenceTransformer (all-MiniLM-L6-v2) | 将文本转为 384 维向量 |
| 向量数据库 | FAISS | 高效的向量相似度检索 |
| 大语言模型 | DeepSeek API | 生成自然语言答案 |
| 文档解析 | PyPDF | 提取 PDF 文本内容 |
| Web 框架 | Streamlit | 快速构建数据应用界面 |

## 📁 项目结构

```
/workspace/
├── rag.py           # 核心 RAG 引擎（检索、生成）
├── pdf_loader.py    # PDF 文档加载模块
├── web.py           # Streamlit Web 界面
├── app.py           # 命令行交互入口
├── tools.py         # 工具函数扩展
├── prompt.py        # Prompt 模板
├── requirements.txt # 项目依赖
└── README.md        # 项目说明
```

## 🚀 快速开始

### 环境准备

```bash
# 克隆项目
git clone https://github.com/xXUEyYin/llm-knowledge-assistant-

# 安装依赖
pip install -r requirements.txt
```

### 配置环境变量

在项目根目录创建 `.env` 文件，配置 API 密钥：

```bash
api_key=your_api_key_here
```

### 运行应用

**方式一：Web 界面**
```bash
streamlit run web.py
```

**方式二：命令行**
```bash
python app.py
```

## 💡 使用示例

### Web 界面使用
1. 启动应用后，在浏览器中打开 Web 界面
2. 在输入框中输入你的问题
3. 点击"发送"按钮
4. 系统将基于知识库返回答案

### 命令行使用
```
请输入问题：如何报销？
回答：公司报销流程需要提交发票...
```

### 工具调用示例
系统支持简单的工具调用，例如查询天气：
```
请输入问题：北京天气怎么样？
回答：北京今天晴天，25°C
```

## 🔧 扩展与定制

### 添加新的工具函数

在 [tools.py](file:///workspace/tools.py#L1-L8) 中添加新的工具函数：

```python
def get_weather(city):
    # 实现工具逻辑
    return weather_data.get(city, "暂无天气数据")
```

### 修改知识库

编辑 `data/company.pdf` 文件或修改 [rag.py](file:///workspace/rag.py#L39-L40) 中的文档加载逻辑。

### 调整检索参数

在 [rag.py](file:///workspace/rag.py#L49) 中修改检索数量：

```python
D, I = index.search(np.array(q_vec), k=3)  # 返回更多结果
```

## 📈 未来规划

- [ ] 持久化向量数据库
- [ ] 支持 OCR 文档识别
- [ ] 多文件批量上传
- [ ] 对话历史记忆功能
- [ ] MCP 协议集成
- [ ] 支持更多文档格式（Word、Markdown 等）
- [ ] 异步处理与任务队列
- [ ] 用户认证与权限管理

## 📝 技术亮点

1. **RAG 架构**：结合检索与生成，提高答案准确性
2. **语义检索**：基于向量相似度，支持自然语言查询
3. **模块化设计**：代码结构清晰，易于维护和扩展
4. **双入口支持**：满足不同场景的使用需求
5. **工具扩展性**：预留工具调用接口，支持功能扩展

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

---

**项目链接**：https://github.com/xXUEyYin/llm-knowledge-assistant-
