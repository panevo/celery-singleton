from importlib.metadata import version

from .singleton import Singleton, clear_locks
from .exceptions import DuplicateTaskError

__version__ = version("celery-singleton-reboot")
