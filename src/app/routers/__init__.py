__all__ = (
    "start_router",
    "register_router",
    "order_router",
    "promos_router",
    "flyers_router"
)

from src.app.routers.start import start_router
from src.app.routers.register import register_router
from src.app.routers.order import order_router
from src.app.routers.promos import promos_router
from src.app.routers.flyers import flyers_router
