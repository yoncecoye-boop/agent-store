from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from config import MODEL

llm = ChatOpenAI(model=MODEL)

def get_trend(topic):
    prompt = ChatPromptTemplate.from_template("""
你是小红书爆款选题专家。

请围绕主题生成一个“高点击选题”，要求：
- 情绪强
- 有冲突
- 有吸引力

主题：{topic}

只返回一句话标题
""")

    chain = prompt | llm
    return chain.invoke({"topic": topic}).content
