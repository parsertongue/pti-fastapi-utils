from __future__ import annotations

from pti.fastapi import env
from pti.fastapi.rest import config
from sqlmodel import SQLModel, Session, create_engine, select
from fastapi import (
    HTTPException,
    Security,
    status,
)
from fastapi.security import APIKeyHeader
import httpx
import typing
import json

__all__ = ["Utils"]


class Utils:
    # see https://stackoverflow.com/a/74401249
    async def get_client():
        # create a new client for each request
        async with httpx.AsyncClient(
            timeout=config.DEFAULT_TIMEOUT, follow_redirects=True
        ) as client:
            # yield the client to the endpoint function
            yield client
            # close the client when the request is done

    API_KEY_HEADER_NAME = "X-API-Key"
    api_key_header = APIKeyHeader(name=API_KEY_HEADER_NAME)

    @staticmethod
    def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
        """Validates API key"""
        if api_key_header in env.API_KEYS:
            return api_key_header
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )

    # @staticmethod
    # def create_db_url(
    #   username: str = env.DB_USERNAME,
    #   password: str = env.DB_PASSWORD,
    #   host: str = proxies.DB_HOST,
    #   port: int = env.DB_PORT,
    #   db_name: str = env.DB_NAME
    # ) -> str:
    #     """Create PostgreSQL DB URL"""
    #     # dialect+driver://username:password@host:port/database_name
    #     return f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"

    # @staticmethod
    # def engine_from_env(
    #   username: str = env.DB_USERNAME,
    #   password: str = env.DB_PASSWORD,
    #   host: str = proxies.DB_HOST,
    #   port: int = env.DB_PORT,
    #   db_name: str = env.DB_NAME,
    #   echo: bool = True
    # ) -> Engine:
    #     """Create SQLAlchemy Engine instance"""
    #     db_url = Utils.create_db_url(
    #       username=username,
    #       password=password,
    #       host=host,
    #       port=port,
    #       db_name=db_name
    #     )
    #     return create_engine(db_url, echo=echo)

    # @staticmethod
    # # NOTE: this is run only once on initialization
    # def create_and_initialize_db(engine: Engine) -> None:
    #     from schema import *
    #     # NOTE: this works because imported basemodels are in scope
    #     SQLModel.metadata.create_all(engine)
