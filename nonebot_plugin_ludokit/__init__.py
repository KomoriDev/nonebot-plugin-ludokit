from nonebot.plugin import PluginMetadata, require, inherit_supported_adapters

require("nonebot_plugin_alconna")

from .config import Config
from .typing import LudoMetadata as LudoMetadata
from .namespace import ludokit_namespace as ludokit_namespace

__plugin_meta__ = PluginMetadata(
    name="LudoKit",
    description="A NoneBot Plugin Library for Building Interactive Games.",
    usage="/ludo",
    type="library",
    config=Config,
    homepage="https://github.com/KomoriDev/nonebot-plugin-ludokit",
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
    extra={
        "unique_name": "LudoKit",
        "author": "Komorebi <mute231010@gmail.com>",
        "version": "0.1.0",
    },
)

from . import matcher as matcher
