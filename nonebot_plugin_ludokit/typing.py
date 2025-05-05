from dataclasses import field, dataclass

from arclet.alconna.typing import CommandMeta


@dataclass(unsafe_hash=True)
class LudoMetadata(CommandMeta):
    name: str = field(default="Unknown")
