import streamlit as st
import time

# ✅ 页面设置
st.set_page_config(
    page_title="张牧川 · AI潜力分析器",
    page_icon="🧠",
    layout="centered"
)

# ✅ 加背景图
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1607746882042-944635dfe10e');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ 自定义按钮样式
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #f63366;
        color: white;
        border-radius: 8px;
        height: 48px;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ 页面Logo + 标题
st.markdown("""
    <div style='text-align: center;'>
        <img src='https://your-logo-url.com/logo.png' width='100'> <!-- 替换为你头像的真实链接 -->
        <h1 style='color: #f63366;'>🧠 AI 潜力分析器</h1>
        <p style='color: gray;'>输入年龄和目标，我来告诉你最适合的AI路径</p>
    </div>
""", unsafe_allow_html=True)

# ✅ 输入区域
with st.container():
    st.markdown("### 👤 请输入你的信息：")
    name = st.text_input("你的名字")
    age = st.number_input("你的年龄", min_value=0, max_value=120, step=1)
    goal = st.text_area("你的目标")

# ✅ 分析逻辑 + 加载动画
if st.button("🚀 开始分析"):
    if name.strip() == "" or goal.strip() == "":
        st.warning("请填写完整信息哦～")
    else:
        with st.spinner('🧠 AI正在思考中...'):
            time.sleep(2)

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

# ✅ 页面底部
st.markdown("""
    <hr>
    <div style='text-align: center; color: gray; font-size: 14px;'>
        本工具由 <b>张牧川</b> 独立开发 ｜ 欢迎体验更多AI神器<br>
        🔗 微信号：xxxxxxx ｜ 🌐 欢迎分享转发
    </div>
""", unsafe_allow_html=True)
