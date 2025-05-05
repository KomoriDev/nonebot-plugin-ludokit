from nonebot_plugin_alconna.uniseg import UniMessage
from nonebot_plugin_alconna.uniseg.segment import I18n
from nonebot_plugin_alconna import Args, Match, Alconna, on_alconna

from .i18n import Lang, lang
from .typing import LudoMetadata
from .config import plugin_config
from .manager import ludokit_manager
from .namespace import ludokit_namespace
from ._extension import CleanDocExtension

ludo = on_alconna(
    Alconna(
        "ludo",
        Args["name?#游戏名称", str],
        namespace=ludokit_namespace,
        meta=LudoMetadata(name="游戏管理器"),
    ),
    block=True,
    use_cmd_start=True,
    extensions=[CleanDocExtension()],
)


@ludo.handle()
async def _(name: Match[str]):
    if name.available:
        meta = ludokit_manager.get_ludo_meta(name.result)
        await ludo.finish(
            f"""
            [{meta.name}]
            {
                meta.description
                if meta.description != "Unknown"
                else Lang.ludo.matcher.no_desc()
            }
            {meta.usage if meta.usage else ""}
            """
        )

    meta_list = ludokit_manager.get_all_ludo_meta()
    last_command = ludokit_manager.peek_last_command()
    await UniMessage(
        [
            I18n(Lang.ludo.matcher.list),
            *(
                f"\n - [{meta.name}]"
                for meta in meta_list
                if not (plugin_config.hide_unknown and meta.name == "Unknown")
            ),
            "\n"
            + lang.require("ludo", "matcher.last_cmd").format(
                name=last_command.meta.__dict__["name"]
            ),
        ]
    ).finish()
