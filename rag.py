from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 初始化模型
model = SentenceTransformer('all-MiniLM-L6-v2')

# 模拟知识库
docs = [
    "我在燕华公司负责设备管理",
    "设备故障处理流程包括报修和检修",
    "物流调度需要优化运输路径"
]

# 向量化
embeddings = model.encode(docs)
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))

def retrieve(query):
    q_vec = model.encode([query])
    D, I = index.search(np.array(q_vec), k=1)
    return docs[I[0][0]]

def get_answer(query):
    context = retrieve(query)
    return f"根据知识库：{context}"
