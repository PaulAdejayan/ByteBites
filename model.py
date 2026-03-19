from __future__ import annotations

from datetime import date
from typing import List, Optional


class MenuItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        """
        Represents a single food item on the menu.

        :param name: the name of the item, cannot be empty
        :param price: non-negative price
        :param category: category string (e.g., 'appetizer')
        :param popularity_rating: between 0.0 and 5.0 inclusive
        """
        if not name:
            raise ValueError("name must be non-empty")
        if price < 0:
            raise ValueError("price must be non-negative")
        if not category:
            raise ValueError("category must be non-empty")
        if not (0.0 <= popularity_rating <= 5.0):
            raise ValueError("popularity_rating must be between 0 and 5")

        self.name: str = name
        self.price: float = price
        self.category: str = category
        self.popularity_rating: float = popularity_rating

    def __repr__(self) -> str:
        return (f"MenuItem(name={self.name!r}, price={self.price!r}, "
                f"category={self.category!r}, popularity_rating={self.popularity_rating!r})")


class Menu:
    def __init__(self, items: Optional[List[MenuItem]] = None):
        """
        Master catalog of all available menu items.

        :param items: initial list of MenuItem objects
        """
        self.items: List[MenuItem] = items[:] if items is not None else []

    def filter_by_category(self, category: str) -> List[MenuItem]:
        """
        Return list of items matching the given category.
        """
        return [item for item in self.items if item.category == category]

    def add_item(self, item: MenuItem) -> None:
        """
        Add a new MenuItem to the menu.
        """
        if not isinstance(item, MenuItem):
            raise TypeError("item must be a MenuItem")
        self.items.append(item)

    def remove_item(self, name: str) -> bool:
        """
        Remove first item with matching name. Return True if removed.
        """
        for i, itm in enumerate(self.items):
            if itm.name == name:
                del self.items[i]
                return True
        return False

    def __repr__(self) -> str:
        return f"Menu(items={self.items!r})"


class Order:
    def __init__(self, items: Optional[List[MenuItem]] = None, order_date: Optional[date] = None):
        """
        Represents a single customer order.

        :param items: list of MenuItem objects
        :param order_date: date when order was placed, defaults to today
        """
        self.items: List[MenuItem] = items[:] if items is not None else []
        self.order_date: date = order_date if order_date is not None else date.today()

    def compute_total(self) -> float:
        """
        Compute total price of all items.
        """
        return sum(item.price for item in self.items)

    def add_item(self, item: MenuItem) -> None:
        if not isinstance(item, MenuItem):
            raise TypeError("item must be a MenuItem")
        self.items.append(item)

    def __repr__(self) -> str:
        return f"Order(items={self.items!r}, order_date={self.order_date!r})"


class Customer:
    def __init__(self, name: str):
        """
        Registered user with name and full order history.
        """
        if not name:
            raise ValueError("name must be non-empty")
        self.name: str = name
        self.purchase_history: List[Order] = []

    def place_order(self, order: Order) -> None:
        if not isinstance(order, Order):
            raise TypeError("order must be an Order")
        self.purchase_history.append(order)

    def total_spent(self) -> float:
        return sum(o.compute_total() for o in self.purchase_history)

    def __repr__(self) -> str:
        return f"Customer(name={self.name!r}, purchase_history={self.purchase_history!r})"

