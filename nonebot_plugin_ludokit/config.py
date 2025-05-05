from pydantic import Field, BaseModel
from nonebot.plugin import get_plugin_config


class ScopedConfig(BaseModel):
    hide_unknown: bool = Field(default=False)


class Config(BaseModel):
    ludokit: ScopedConfig = Field(default_factory=ScopedConfig)
    """LudoKit Plugin Config"""


plugin_config = get_plugin_config(Config).ludokit
