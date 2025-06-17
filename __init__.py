# -*- coding: utf-8 -*-

import logging

from core import create_hardlink
from tui_browser import LinkerTUI 
from logger_utils import get_logger
from config import *

# Add debug log to LinkerTUI __init__ for diagnostic purposes
original_init = LinkerTUI.__init__
def debug_init(self, *args, **kwargs):
    logger = get_logger("linker.tui")
    logger.debug("LinkerTUI __init__ called")
    original_init(self, *args, **kwargs)
LinkerTUI.__init__ = debug_init

__all__ = ['create_hardlink', 'LinkerTUI', 'get_logger']
