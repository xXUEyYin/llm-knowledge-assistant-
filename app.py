from rag import get_answer

print("AI知识库助手启动（输入 exit 退出）")

while True:
    query = input("请输入问题：")
    if query == "exit":
        break
    answer = get_answer(query)
    print("回答：", answer)