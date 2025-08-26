import streamlit as st
from test import generate_text
st.title("爆款小红书AI写作助手🖊")
with st.sidebar:
    openai_api_key=st.text_input("请输入openai_api密钥🔑",type="password")
title=st.text_input("请输入主题💡")
creativity=st.slider("请输入写作创造力",value=0.2,min_value=0.0,max_value=1.0,step=0.1)
submit=st.button("开始写作")
if submit and not openai_api_key:
    st.info("请输入openai_api_key")
    st.stop()
if submit and not title:
    st.info("请输入主题")
    st.stop()
if submit:
    st.write("正在思考中🤔")
    st.write(generate_text(title,creativity,openai_api_key))

