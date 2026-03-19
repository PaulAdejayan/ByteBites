import pytest
from datetime import date
from model import MenuItem, Menu, Order, Customer


# ── MenuItem Tests ─────────────────────────────────────


def test_menuitem_stores_attributes():
    item = MenuItem("Spicy Burger", 9.99, "Mains", 4.5)
    assert item.name == "Spicy Burger"
    assert item.price == 9.99
    assert item.category == "Mains"
    assert item.popularity_rating == 4.5


def test_menuitem_rejects_empty_name():
    with pytest.raises(ValueError):
        MenuItem("", 5.00, "Drinks", 3.0)


def test_menuitem_rejects_negative_price():
    with pytest.raises(ValueError):
        MenuItem("Soda", -1.00, "Drinks", 3.0)


def test_menuitem_rejects_invalid_rating():
    with pytest.raises(ValueError):
        MenuItem("Soda", 2.00, "Drinks", 6.0)


# ── Menu Tests ─────────────────────────────────────────


def test_filter_by_category_returns_matching_items():
    burger = MenuItem("Burger", 9.99, "Mains", 4.5)
    soda = MenuItem("Soda", 2.49, "Drinks", 4.0)
    wrap = MenuItem("Wrap", 8.49, "Mains", 4.2)
    menu = Menu([burger, soda, wrap])

    mains = menu.filter_by_category("Mains")
    assert len(mains) == 2
    assert burger in mains
    assert wrap in mains


def test_filter_by_category_returns_empty_for_no_match():
    menu = Menu([MenuItem("Burger", 9.99, "Mains", 4.5)])
    assert menu.filter_by_category("Desserts") == []


def test_menu_starts_empty_by_default():
    menu = Menu()
    assert menu.items == []


# ── Order Tests ────────────────────────────────────────


def test_order_total_with_multiple_items():
    burger = MenuItem("Burger", 10.00, "Mains", 4.5)
    soda = MenuItem("Soda", 5.00, "Drinks", 4.0)
    order = Order([burger, soda])
    assert order.compute_total() == 15.00


def test_order_total_is_zero_when_empty():
    order = Order()
    assert order.compute_total() == 0.0


def test_order_defaults_to_today():
    order = Order()
    assert order.order_date == date.today()


def test_order_accepts_custom_date():
    custom = date(2026, 1, 15)
    order = Order(order_date=custom)
    assert order.order_date == custom


# ── Customer Tests ─────────────────────────────────────


def test_customer_starts_with_empty_history():
    c = Customer("Alice")
    assert c.name == "Alice"
    assert c.purchase_history == []


def test_customer_place_order_adds_to_history():
    c = Customer("Alice")
    order = Order([MenuItem("Burger", 10.00, "Mains", 4.5)])
    c.place_order(order)
    assert len(c.purchase_history) == 1


def test_customer_total_spent():
    c = Customer("Alice")
    c.place_order(Order([MenuItem("Burger", 10.00, "Mains", 4.5)]))
    c.place_order(Order([MenuItem("Soda", 5.00, "Drinks", 4.0)]))
    assert c.total_spent() == 15.00


def test_customer_total_spent_with_no_orders():
    c = Customer("Bob")
    assert c.total_spent() == 0.0


def test_customer_rejects_empty_name():
    with pytest.raises(ValueError):
        Customer("")
