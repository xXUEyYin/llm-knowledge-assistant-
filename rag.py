import os
from dotenv import load_dotenv
from tools import get_weather
from pdf_loader import load_pdf

# 从 .env 文件加载环境变量
load_dotenv()

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from openai import OpenAI

# 初始化模型
model = SentenceTransformer('all-MiniLM-L6-v2')

# 初始化大模型客户端（这里用兼容写法）
api_key = os.environ.get('api_key') or os.environ.get('OPENAI_API_KEY')
if not api_key:
    raise ValueError("请设置环境变量 api_key 或 OPENAI_API_KEY")

client = OpenAI(
    api_key="sk-f3d578d029464c368023c2645dd5958d",
    base_url="https://api.deepseek.com")

def split_text(text, chunk_size=300):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks

# 知识库
#docs = [
#    "公司报销流程需要提交发票",
#    "员工请假需要提前一天申请",
#    "设备故障需要联系技术部门"
#]

pdf_text = load_pdf("data/company.pdf")
docs = split_text(pdf_text)

# 向量化
embeddings = model.encode(docs)
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))

def retrieve(query):
    q_vec = model.encode([query])
    D, I = index.search(np.array(q_vec), k=2)
    return [docs[i] for i in I[0]]

def build_prompt(context_list, query):
    context = "\n".join(context_list)
    return f"""
你是企业知识助手，请严格基于以下内容回答问题：

【知识库】
{context}

【问题】
{query}

要求：
1. 只基于知识库回答
2. 简洁清晰
"""

def get_answer(query):
        # MCP工具调用（模拟）
    if "天气" in query:

        if "北京" in query:
            return get_weather("北京")

        elif "上海" in query:
            return get_weather("上海")

        elif "三亚" in query:
            return get_weather("三亚")
    # 正常RAG流程        
    context_list = retrieve(query)
    prompt = build_prompt(context_list, query)

    response = client.chat.completions.create(
    model="deepseek-v4-pro",# 或其他模型
    messages=[
    {"role": "system", "content": "You are a helpful assistant"},  # 系统消息：设定AI身份
    {"role": "user", "content": prompt}  # 用户消息：实际的问题
    ],
    stream=False,
    reasoning_effort="high",
)

    return response.choices[0].message.content