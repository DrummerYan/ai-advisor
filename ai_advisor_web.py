import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="张牧川 · AI潜力分析器",
    page_icon="🧠",
    layout="centered"
)

# 页面顶部样式（大标题）
st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <h1 style='color: #f63366;'>🧠 AI 潜力分析器</h1>
        <p style='color: gray;'>根据你的年龄与目标，智能分析你的AI创业路径</p>
    </div>
""", unsafe_allow_html=True)

# 输入卡片样式开始
with st.container():
    st.markdown("### 👤 请输入你的信息：")
    name = st.text_input("你的名字")
    age = st.number_input("你的年龄", min_value=0, max_value=120, step=1)
    goal = st.text_area("你的目标")

# 分析逻辑
if st.button("🚀 开始分析"):
    if name.strip() == "" or goal.strip() == "":
        st.warning("请填写完整信息哦～")
    else:
        st.markdown("---")
        st.markdown("### 🧠 分析结果：")

        if age < 18:
            st.success(f"💡 {name}，你才 {age} 岁，未来无限可能，现在是学习AI最好的时机！建议先打好基础，1-2年后开始实战项目。")
        elif age <= 35:
            if "赚钱" in goal or "一人公司" in goal:
                st.success(f"🔥 {name}，你正当年（{age}岁），目标非常清晰：{goal}。建议立刻执行，从AI工具、自动化、SaaS切入，快速测试市场！")
            else:
                st.success(f"✅ {name}，{age}岁正适合深耕目标：{goal}，建议你用AI加速落地，把时间价值最大化！")
        else:
            st.success(f"🕰️ {name}，你 {age} 岁了，但经验是最大财富！目标是：{goal}，建议你结合AI+你熟悉的行业，做出独一无二的价值型项目。")

# 底部署名 + 引导
st.markdown("""
    <hr>
    <div style='text-align: center; color: gray; font-size: 14px;'>
        本工具由 <b>张牧川</b> 独立开发 ｜ 欢迎体验更多AI神器<br>
        🔗 微信号：xxxxxxx ｜ 🌐 欢迎分享转发
    </div>
""", unsafe_allow_html=True)
