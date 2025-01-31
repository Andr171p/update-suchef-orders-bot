__all__ = (
    "start_router",
    "register_router",
    "orders_router",
    "promos_router",
    "bonus_router"
)

from src.app.routers.start import start_router
from src.app.routers.register import register_router
from src.app.routers.orders import orders_router
from src.app.routers.promos import promos_router
from src.app.routers.bonus import bonus_router
