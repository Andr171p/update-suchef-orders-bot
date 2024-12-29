__all__ = (
    "start_kb",
    "menu_kb",
    "promo_page_kb",
    "pay_link_kb",
    "confirmed_link_kb"
)

from src.app.keyboards.start import start_kb
from src.app.keyboards.menu import menu_kb
from src.app.keyboards.promos import promo_page_kb
from src.app.keyboards.payment import pay_link_kb, confirmed_link_kb
