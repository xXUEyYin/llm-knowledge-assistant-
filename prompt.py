def build_prompt(context, query):
    return f"""
你是企业知识助手，请基于以下内容回答问题：

{context}

问题：{query}
"""