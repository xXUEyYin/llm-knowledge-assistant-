# LLM Knowledge Assistant

一个基于RAG的AI知识库问答系统

## 功能
- 文档检索
- 智能问答
- 简单对话

## 技术
- SentenceTransformer
- FAISS
- Python

## 运行
pip install -r requirements.txt
python app.py
## 🔥 升级：接入大模型API

本项目已接入大语言模型（LLM），实现完整RAG流程：

用户问题 → 向量检索 → 上下文构建 → LLM生成答案

相比传统检索，回答更加自然、准确。
