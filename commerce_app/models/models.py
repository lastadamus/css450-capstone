"""Models for commerce_app objects"""


class BaseUser:
    """User model for users accessing application"""

    id: str
    email_address: str
    user_name: str
    f_name: str = ""
    l_name: str = ""
    address: dict[str, str]
    created_date: str


class BaseItem:
    """Item model for items being sold in application"""

    id: str
    item_name: str
    item_type: str
    item_price: float = 0.00
    item_qty: int = 0


class BaseCart:
    """Cart model for container of Items being sold"""

    id: str
    items: list[str]


class BaseTransaction:
    """Transaction model for storing transaction data from app"""

    id: str
    cart_id: str
    customer_id: str
    transact_date: str = ""
