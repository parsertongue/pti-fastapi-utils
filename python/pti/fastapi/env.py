# -*- coding: utf-8 -*-
"""
env vars.
"""

import os


VERSION: str = os.environ.get("APP_VERSION", "????")

DEFAULT_API_KEY = "TEST_MODE"

def keys_from_env() -> list[str]:
    """parses API_KEYS env variable.
    If the ENV variable isn't set,
    we'll default to a single key
    (see `DEFAULT_API_KEY`)
    """
    res = [
        key.strip()
        for key in os.environ.get("API_KEYS", "").split(",")
        if len(key.strip()) > 0
    ]
    if len(res) == 0 or res[0] == None:
        return [DEFAULT_API_KEY]
    return res


API_KEYS: list[str] = keys_from_env()