from rag.retriever import get_retriever
from agents.router import route_query
from agents.answer import answer_with_context
from agents.critic import critic_check
from langchain.chat_models import ChatOpenAI
from config import MODEL

llm = ChatOpenAI(model=MODEL)

def direct_answer(query):
    return llm.invoke(query).content

def run():
    retriever = get_retriever()

    while True:
        query = input("\n请输入问题（exit退出）：")

        if query == "exit":
            break

        route = route_query(query)
        print(f"🧭 路由选择：{route}")

        if route == "RAG":
            docs = retriever.get_relevant_documents(query)
            answer = answer_with_context(query, docs)
        else:
            answer = direct_answer(query)

        check = critic_check(query, answer)

        if check == "PASS":
            print("\n✅ 最终回答：\n", answer)
        else:
            print("\n⚠️ 回答不可靠，建议重新提问")

if __name__ == "__main__":
    run()
