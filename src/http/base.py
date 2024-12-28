from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class BaseClient(ABC):
    @abstractmethod
    async def get(
            self,
            url: str,
            headers: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any] | None: pass

    @abstractmethod
    async def post(
            self,
            url: str,
            json: Dict[str, Any],
            headers: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any] | None: pass
