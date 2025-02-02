# -*- coding: utf-8 -*-
"""
ENV-based config
"""

import os


DEFAULT_TIMEOUT = float(os.environ.get("DEFAULT_TIMEOUT", "180.0"))
