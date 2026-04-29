from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from config import MODEL

llm = ChatOpenAI(model=MODEL)

def critic_check(query, answer):
    prompt = ChatPromptTemplate.from_template("""
你是一个审核Agent。

判断下面回答是否存在“编造”或“不基于事实”的情况。
如果有问题，返回 "REJECT"
如果可信，返回 "PASS"

问题：
{query}

回答：
{answer}
""")

    chain = prompt | llm
    result = chain.invoke({
        "query": query,
        "answer": answer
    })
    return result.content.strip()
