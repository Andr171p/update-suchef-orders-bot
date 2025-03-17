from contextlib import asynccontextmanager
from contextlib import AbstractAsyncContextManager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    pass
