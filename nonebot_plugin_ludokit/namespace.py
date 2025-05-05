from arclet.alconna.config import Namespace, config

from .formatter import LudoTextFormatter

ludokit_namespace = Namespace(
    name="ludokit",
    formatter_type=LudoTextFormatter,
)
config.namespaces["ludokit"] = ludokit_namespace
