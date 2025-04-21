from os import getenv
from typing import Union

from dotenv import load_dotenv
from fastqqbot import Client

from botpy import Intents
from botpy.ext.command_util import Commands
from botpy.message import Message, GroupMessage


class BotClient(Client):
    # 配置指令回复
    @Commands("你好")
    async def hello(self, message: Union[Message, GroupMessage], params: str):
        # params: 指令传入的参数文本

        print(f"指令：你好")
        print(f"参数：{params}")

        # 根据指令及传入的参数文本回复信息回复
        content = f"你好! {params}"

        print(f"返回：{content}")

        await self.post_message(message=message, content=content)

    async def on_create(self, message: Union[Message, GroupMessage]):
        # 注册函数
        await self.hello(message=message)


if __name__ == "__main__":
    # 加载本地环境变量
    load_dotenv()

    # 获取 AppID / AppSecret
    APP_ID = getenv("APP_ID")
    APP_SECRET = getenv("APP_SECRET")

    # 启动 QQ 机器人客户端
    intents = Intents.default()
    client = BotClient(intents=intents)
    client.run(appid=APP_ID, secret=APP_SECRET)
