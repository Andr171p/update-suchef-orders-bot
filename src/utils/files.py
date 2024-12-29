import json
import aiofiles

from pathlib import Path
from typing import Dict, Any


def load_txt(path: Path | str) -> str:
    with open(
        file=path,
        mode="r",
        encoding="utf-8"
    ) as file:
        return file.read()


async def load_txt_async(path: Path | str) -> str:
    async with aiofiles.open(
        file=path,
        mode="r",
        encoding="utf-8"
    ) as file:
        return await file.read()


def load_json(path: Path | str) -> Dict[str, Any]:
    with open(
        file=path,
        mode="r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


async def load_json_async(path: Path | str) -> Dict[str, Any]:
    async with aiofiles.open(
        file=path,
        mode='r',
        encoding='utf-8'
    ) as file:
        data = await file.read()
        return json.loads(data)
