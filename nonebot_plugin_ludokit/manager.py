from arclet.alconna.core import Alconna
from arclet.alconna.manager import command_manager
from nonebot_plugin_alconna.matcher import AlconnaMatcher

from .typing import LudoMetadata


class LudokitManager:
    def __init__(self) -> None: ...

    @property
    def commands(self) -> list[Alconna]:
        return command_manager.get_commands("ludokit")

    def referent(self, command: Alconna) -> type[AlconnaMatcher] | None:
        if "matcher" in command.meta.extra:
            try:
                return command.meta.extra["matcher"]()
            except KeyError:
                return None
        return None

    def peek_last_command(self) -> Alconna:
        record = command_manager.records.items()[-1]
        return record[1].source

    def get_ludo_meta(self, name: str) -> LudoMetadata:
        for command in self.commands:
            if str(command.meta.__dict__.get("name", "")).lower() == name.lower():
                return LudoMetadata(**command.meta.__dict__)
        return LudoMetadata()

    def get_all_ludo_meta(self) -> list[LudoMetadata]:
        return [LudoMetadata(**command.meta.__dict__) for command in self.commands]


ludokit_manager = LudokitManager()
