import sys

from . import utils

from loguru import logger as log
log.remove(0)
log.add(sys.stderr, level="CRITICAL")