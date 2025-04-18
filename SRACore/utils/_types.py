import sys

# type hints for SRACore

from typing import Callable, Any
Point = tuple[float, float]
Config = dict
TaskCall = Callable[..., None]
MetaData = dict
TaskArgv = dict[str, Any]
