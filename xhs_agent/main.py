from agents.trend import get_trend
from agents.copywriting import generate_copy
from agents.image_prompt import generate_image_prompt

def run():
    topic = input("输入你想做的领域（如：减肥/学习/赚钱）：")

    trend = get_trend(topic)
    print("\n🔥 热点选题：", trend)

    copy = generate_copy(trend)
    print("\n📝 爆款文案：\n", copy)

    prompt = generate_image_prompt(trend)
    print("\n🎨 配图提示词：\n", prompt)

if __name__ == "__main__":
    run()
