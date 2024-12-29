__all__ = (
    "start_router",
    "auth_router",
    "order_router",
    "promos_router"
)

from src.app.routers.start import start_router
from src.app.routers.auth import auth_router
from src.app.routers.order import order_router
from src.app.routers.promos import promos_router
