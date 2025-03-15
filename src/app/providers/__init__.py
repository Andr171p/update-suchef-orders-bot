__all__ = (
    "UserServiceProvider",
    "OrdersServiceProvider",
    "BonusServiceProvider",
    "PromoServiceProvider"
)

from src.app.providers.user_service import UserServiceProvider
from src.app.providers.orders_service import OrdersServiceProvider
from src.app.providers.bonus_service import BonusServiceProvider
from src.app.providers.promo_service import PromoServiceProvider
