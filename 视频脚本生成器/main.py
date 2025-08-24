import streamlit as st
from mm import generate_script
st.title("🎞视频脚本生成器")
with st.sidebar:
    openai_api_key=st.text_input("请输入openai api密钥:",type="password")
    st.markdown("[获取openai api key](https://openai.google/doc/research/openai-api-key.html)")
subject=st.text_input("💡请输入视频的主题")
video_length=st.number_input("⏰请输入视频的大致时长（单位：分钟）",max_value=10.0,min_value=0.1,step=0.1)
creativity=st.slider("⭐请输入视频脚本的创造力",min_value=0.0,max_value=1.0,value=0.2,step=0.1)
submit=st.button("生成文本")
if submit and not openai_api_key:
    st.info("请输入你的openai api密钥")
    st.stop()
if submit and not subject:
    st.info("请输入视频主题")
    st.stop()
if submit:
    with st.spinner(("正在思考中，请稍后...")):
        title,script=generate_script(subject,video_length,creativity,openai_api_key)
    st.success("视频脚本已生成!")
    st.subheader("🍒标题:")
    st.write(title)
    st.subheader("📜视频脚本:")
    st.write(script)

