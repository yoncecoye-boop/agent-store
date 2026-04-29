from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from config import MODEL

llm = ChatOpenAI(model=MODEL)

def generate_image_prompt(title):
    prompt = ChatPromptTemplate.from_template("""
你是视觉设计专家。

根据标题生成适合AI绘图的提示词：
- 风格：小红书爆款
- 人物表情夸张
- 场景真实

标题：{title}
""")

    chain = prompt | llm
    return chain.invoke({"title": title}).content
