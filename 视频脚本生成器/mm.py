from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
def generate_script(subject,video_length,
                    creativity,api_key):
    title_template=ChatPromptTemplate.from_messages(
        [
            ("human","请为{subject}这个主题的视频想一个吸引人的标题,使用中文")
        ]
    )
    script_template=ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个视频脚本。
             视频标题：{title}，视频时长：{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
             要求开头抓住眼球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头、中间，结尾】分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人。必须使用中文
             """
             )
        ]
    )
    model=ChatOpenAI(openai_api_key=api_key,temperature=creativity,
                     openai_api_base="https://api.aigc369.com/v1")
    title_chain=title_template|model
    title=title_chain.invoke({"subject":subject}).content
    script_chain=script_template|model
    script=script_chain.invoke({"title":title,
                                "duration":video_length,
                                }).content
    return title,script
# print(generate_script("书包",1,0.7,"sk-qamG0kZHy8MGVcBtWUldkMypr4t3na76sDYO1Mza5OtNgm5Z"))


