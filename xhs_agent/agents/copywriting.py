from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from config import MODEL

llm = ChatOpenAI(model=MODEL)

def generate_copy(title):
    prompt = ChatPromptTemplate.from_template("""
你是小红书爆款文案专家。

根据标题生成内容：
- 开头强吸引（反常识/情绪）
- 中间给干货
- 结尾引导互动

标题：{title}
""")

    chain = prompt | llm
    return chain.invoke({"title": title}).content
