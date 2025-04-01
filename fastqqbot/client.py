from typing import Union

from botpy import Client as BaseClient
from botpy.message import Message, GroupMessage
from botpy.types.message import Message as BaseMessage


__all__ = ["Client"]


class Client(BaseClient):
    async def post_message(
        self, message: Union[Message, GroupMessage], **kwargs
    ) -> BaseMessage:
        if isinstance(message, GroupMessage) and isinstance(message.group_openid, str):
            group_openid: str = message.group_openid
            return await self.api.post_group_message(
                group_openid=group_openid, msg_id=message.id, **kwargs
            )
        elif isinstance(message, Message) and isinstance(message.channel_id, str):
            channel_id: str = message.channel_id
            return await self.api.post_message(
                channel_id=channel_id, msg_id=message.id, **kwargs
            )
        else:
            raise ValueError("Invalid message type")

    async def on_create(self, message: Union[Message, GroupMessage]):
        pass

    async def on_at_message_create(self, message: Message):
        await self.on_create(message)

    async def on_group_at_message_create(self, message: GroupMessage):
        await self.on_create(message)
