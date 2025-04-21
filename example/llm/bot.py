from os import getenv
from typing import Union

from dotenv import load_dotenv
from fastqqbot import Client
from openai import AsyncOpenAI

from botpy import Intents
from botpy.ext.command_util import Commands
from botpy.message import Message, GroupMessage


class BotClient(Client):
    # 配置指令回复
    @Commands("LLM")
    async def llm(self, message: Union[Message, GroupMessage], params: str):
        # params: 指令传入的参数文本

        print(f"指令：LLM")
        print(f"参数：{params}")

        # 将指令及传入的参数文本回复信息发送至 LLM API
        completion = await openai.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": params
                }
            ]
        )

        # 获取 LLM API 返回的内容
        content = completion.choices[0].message.content

        print(f"返回：{content}")

        await self.post_message(message=message, content=content)

    async def on_create(self, message: Union[Message, GroupMessage]):
        # 注册函数
        await self.llm(message=message)


if __name__ == "__main__":
    # 加载本地环境变量
    load_dotenv()

    # 获取 AppID / AppSecret
    APP_ID = getenv("APP_ID")
    APP_SECRET = getenv("APP_SECRET")

    # 获取 OpenAI API 密钥和 URL
    BASE_URL = getenv("BASE_URL")
    API_KEY = getenv("API_KEY")
    MODEL_NAME = getenv("MODEL_NAME")

    # 初始化 OpenAI 客户端
    openai = AsyncOpenAI(
        api_key=API_KEY,
        base_url=BASE_URL,
    )

    # 启动 QQ 机器人客户端
    intents = Intents.default()
    client = BotClient(intents=intents)
    client.run(appid=APP_ID, secret=APP_SECRET)
