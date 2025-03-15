import re


def is_valid_phone(phone: str) -> bool:
    pattern = r'\+\d$\d{3}$\d{3}-\d{2}-\d{2}'
    return bool(re.fullmatch(
        pattern=pattern,
        string=phone
    ))
