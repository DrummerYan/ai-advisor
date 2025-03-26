import streamlit as st

st.set_page_config(
    page_title="张牧川 · AI潜力分析器",
    page_icon="🧠",
    layout="centered"
)

st.markdown("<h1 style='text-align: center; color: pink;'>🧠 AI 潜力分析器</h1>", unsafe_allow_html=True)
st.markdown("---")

name = st.text_input("👤 请输入你的名字：")
age = st.number_input("📅 请输入你的年龄：", min_value=0, max_value=120, step=1)
goal = st.text_area("🎯 请输入你的目标：")

if st.button("🚀 开始分析"):
    if age < 18:
        st.success(f"💡 {name}，你才 {age} 岁，未来无限可能，现在是学习AI最好的时机！建议先打好基础，1-2年后开始实战项目。")
    elif age <= 35:
        if "赚钱" in goal or "一人公司" in goal:
            st.success(f"🔥 {name}，你正当年（{age}岁），目标非常清晰：{goal}。建议立刻执行，从AI工具、自动化、SaaS切入，快速测试市场！")
        else:
            st.success(f"✅ {name}，{age}岁正适合深耕目标：{goal}，建议你用AI加速落地，把时间价值最大化！")
    else:
        st.success(f"🕰️ {name}，你 {age} 岁了，但经验是最大财富！目标是：{goal}，建议你结合AI+你熟悉的行业，做出独一无二的价值型项目。")
