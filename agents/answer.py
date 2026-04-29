from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from config import MODEL

llm = ChatOpenAI(model=MODEL)

def answer_with_context(query, docs):
    context = "\n\n".join([d.page_content for d in docs])

    prompt = ChatPromptTemplate.from_template("""
你是企业知识助手，请基于以下内容回答问题，并给出引用依据：

{context}

问题：
{query}
""")

    chain = prompt | llm
    return chain.invoke({
        "context": context,
        "query": query
    }).content
