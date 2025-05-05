from . import driver
from .manager import ludokit_manager
from ._extension import LudokitExtension


@driver.on_startup
async def inject_extension():
    commands = ludokit_manager.commands
    for command in commands:
        matcher = ludokit_manager.referent(command)
        if matcher is None:
            return
        matcher._rule.executor.extensions.append(LudokitExtension())
