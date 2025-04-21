from os import getenv
from typing import Union

from dotenv import load_dotenv
from fastqqbot import Client

from botpy import Intents
from botpy.ext.command_util import Commands
from botpy.message import Message, GroupMessage


class BotClient(Client):
    # In QQ Channel or Group: @{Bot Name} /{Commands} {params} like this: @{Bot Name} /Test Hello
    @Commands("Test")
    async def test(self, message: Union[Message, GroupMessage], params: str):
        # Reply a message with the parameters received
        await self.post_message(message=message, content=f"Hello! {params}")

    async def on_create(self, message: Union[Message, GroupMessage]):
        # Register the command when a message is created
        await self.test(message=message)


if __name__ == "__main__":
    load_dotenv()
    appid = getenv("APP_ID")
    secret = getenv("APP_SECRET")

    intents = Intents.default()
    client = BotClient(intents=intents)
    client.run(appid=appid, secret=secret)
