# import streamlit as st
# st.markdown("<h1 style='text-align: center;'>QQ登录</h1>", unsafe_allow_html=True)
# count=st.text_input("账号")
# password=st.text_input("密码",type='password')
# b=st.button("登录")
# if b:
#     st.markdown("<h1 style='text-align: center;'>登录成功</h1>", unsafe_allow_html=True)
import streamlit as st

# 自定义CSS样式
st.markdown("""
    <style>
    .login-button {
        padding: 0.6rem 0;  /* 调整按钮内边距控制高度 */
        font-size: 1rem;   /* 按钮文字大小 */
    }
    .input-label {
        font-weight: 500;
        margin-bottom: 0.3rem;
    }
    </style>
""", unsafe_allow_html=True)

# 页面配置
st.set_page_config(page_title="QQ登录", page_icon="🐧", layout="centered")

# 居中标题
st.markdown("<h1 style='text-align: center; color: #1677ff;'>QQ登录</h1>", unsafe_allow_html=True)

# 创建登录表单
with st.form("login_form", clear_on_submit=False):
    # 账号输入
    st.markdown("<p class='input-label'>账号</p>", unsafe_allow_html=True)
    username = st.text_input("", placeholder="请输入QQ号码或邮箱", key="username")

    # 密码输入
    st.markdown("<p class='input-label'>密码</p>", unsafe_allow_html=True)
    password = st.text_input("", placeholder="请输入密码", type="password", key="password")

    # 调整按钮大小和居中
    col1, col2, col3 = st.columns([1, 2, 1])  # 中间列宽度决定按钮宽度
    with col2:
        submit_btn = st.form_submit_button(
            "登录",
            use_container_width=True,
            args=("login-button",)
        )

# 处理登录逻辑
if submit_btn:
    if not username:
        st.error("请输入账号")
    elif not password:
        st.error("请输入密码")
    else:
        # 这里可以添加实际验证逻辑
        st.success(f"账号: {username} 验证中...")
        # 示例：简单验证
        if username == "123456" and password == "password":
            st.success("登录成功！")
        else:
            st.error("账号或密码错误")

# 底部链接
st.markdown("""
    <div style='text-align: center; margin-top: 1rem;'>
        <a href='#' style='color: #1677ff; margin-right: 1rem;'>忘记密码?</a>
        <a href='#' style='color: #1677ff;'>注册账号</a>
    </div>
""", unsafe_allow_html=True)
print(username)
print(password)