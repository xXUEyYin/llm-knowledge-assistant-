from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 初始化模型
model = SentenceTransformer('all-MiniLM-L6-v2')

# 模拟知识库
docs = [
    "公司报销流程需要提交发票",
    "员工请假需要提前一天申请",
    "设备故障需要联系技术部门"
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