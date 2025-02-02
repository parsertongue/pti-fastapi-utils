# -*- coding: utf-8 -*-
"""
Response models for API
"""
from __future__ import annotations
from dataclasses import dataclass
from fastapi.responses import Response
from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum
import typing

__all__ = [
    "Utf8TextResponse"
]

class Utf8TextResponse(Response):
    media_type = "text/plain; charset=utf-8"