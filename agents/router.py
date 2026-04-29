from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from config import MODEL

llm = ChatOpenAI(model=MODEL)

def route_query(query: str):
    prompt = ChatPromptTemplate.from_template("""
你是一个路由Agent。
判断用户问题属于：
1. 知识库问题（返回 "RAG"）
2. 常识问题（返回 "DIRECT"）

问题：
{query}
只返回一个词。
""")

    chain = prompt | llm
    result = chain.invoke({"query": query})
    return result.content.strip()
