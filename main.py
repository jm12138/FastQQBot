from typing import Union
from argparse import ArgumentParser

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
    parser = ArgumentParser()

    parser.add_argument("--appid", type=str, help="AppID")
    parser.add_argument("--secret", type=str, help="Secret")

    args = parser.parse_args()

    appid = args.appid
    secret = args.secret

    intents = Intents.default()
    client = BotClient(intents=intents)
    client.run(appid=appid, secret=secret)
