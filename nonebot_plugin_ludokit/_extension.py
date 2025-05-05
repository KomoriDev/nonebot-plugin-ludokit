import inspect

from nonebot_plugin_alconna.uniseg import UniMessage
from nonebot_plugin_alconna.extension import Extension
from nonebot.internal.adapter import Bot, Event, Message


class CleanDocExtension(Extension):
    @property
    def priority(self) -> int:
        return 15

    @property
    def id(self) -> str:
        return "CleanDoc"

    async def send_wrapper(
        self, bot: Bot, event: Event, send: str | Message | UniMessage
    ):
        plain_text = (
            send if isinstance(send, Message | UniMessage) else inspect.cleandoc(send)
        )
        return plain_text
