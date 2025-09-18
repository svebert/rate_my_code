from .core import rate_my_code
from .fish import rate_my_cod
from .kot import rate_my_kot
from .pylint import run_pylint

__all__ = ["rate_my_code", "rate_my_cod", "rate_my_kot", "run_pylint"]

from ._version import version as __version__