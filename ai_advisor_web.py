import streamlit as st
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ---------------- 页面配置 ----------------
st.set_page_config(
    page_title="张牧川 · AI潜力分析器",
    page_icon="🧠",
    layout="centered"
)

# ---------------- 样式设置 ----------------
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1607746882042-944635dfe10e");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    div.stButton > button:first-child {
        background-color: #f63366;
        color: white;
        border-radius: 12px;
        height: 48px;
        font-size: 18px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Logo 和标题 ----------------
st.markdown("""
    <div style='text-align: center; margin-top: 30px; margin-bottom: 30px;'>
        <img src='https://cdn-icons-png.flaticon.com/512/4712/4712039.png' width='80'>
        <h1 style='color: #f63366; font-size: 36px;'>AI 潜力分析器</h1>
        <p style='color: gray; font-size: 16px;'>输入年龄和目标，我来告诉你最适合的AI路径</p>
    </div>
""", unsafe_allow_html=True)

# ---------------- 表单输入 ----------------
with st.container():
    st.markdown("### 👤 请输入你的信息：")
    name = st.text_input("你的名字")
    age = st.number_input("你的年龄", min_value=0, max_value=120, step=1)
    goal = st.text_area("你的目标")

# ---------------- 按钮逻辑 ----------------
if st.button("🚀 开始分析"):
    if name.strip() == "" or goal.strip() == "":
        st.warning("请填写完整信息哦～")
    else:
        with st.spinner("🧠 AI正在思考中，请稍等..."):
            time.sleep(2)

        st.markdown("---")
        st.markdown("### 🧠 分析结果：")

        if age < 18:
            suggestion = f"💡 {name}，你才 {age} 岁，未来无限可能，现在是学习AI最好的时机！建议先打好基础，1-2年后开始实战项目。"
        elif age <= 35:
            if "赚钱" in goal or "一人公司" in goal:
                suggestion = f"🔥 {name}，你正当年（{age}岁），目标非常清晰：{goal}。建议立刻执行，从AI工具、自动化、SaaS切入，快速测试市场！"
            else:
                suggestion = f"✅ {name}，{age}岁正适合深耕目标：{goal}，建议你用AI加速落地，把时间价值最大化！"
        else:
            suggestion = f"🕰️ {name}，你 {age} 岁了，但经验是最大财富！目标是：{goal}，建议你结合AI+你熟悉的行业，做出独一无二的价值型项目。"

        st.success(suggestion)

        # ---------------- 写入 Google 表格 ----------------
        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
            client = gspread.authorize(creds)

            sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1CwdVWWNhCC3xB18L9JmI6ZRJI1UOwZxhWpLiDXvkoZY/edit")
            worksheet = sheet.get_worksheet(0)  # 默认第一个工作表

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            worksheet.append_row([name, age, goal, suggestion, now])

        except Exception as e:
            st.error(f"❌ 写入 Google 表格失败：{e}")

# ---------------- 底部引导信息 ----------------
st.markdown("""
    <hr style='margin-top:50px; margin-bottom:10px;'>
    <div style='text-align: center; font-size: 14px; color: gray;'>
        本工具由 <b>张牧川</b> 独立开发 ｜ 微信：xxxxxx ｜ 欢迎分享使用<br>
        🚀 一人公司 · AI 工具集 正在建设中…
    </div>
""", unsafe_allow_html=True)
