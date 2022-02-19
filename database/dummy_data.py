from decimal import Decimal

from data_classes import Alerts, Items, Price_History, User
from methods import add_alert, add_item, add_price_history, add_user


def mock_data(conn):

    # mock user
    person1 = User(email="will@gmail.com", password="password123")
    person2 = User(email="tom@gmail.com", password="password123")
    person3 = User(email="tia@gmail.com", password="password123")
    person4 = User(email="sally@gmail.com", password="password123")
    add_user(conn, person1)
    add_user(conn, person2)
    add_user(conn, person3)
    add_user(conn, person4)

    # mock item
    a = Items(
        asin="B07SVVP426",
        title="item title 1",
        current_amount=Decimal(4.20),
        currency="£",
    )
    b = Items(
        asin="B07G3QKNCQ",
        title="item title 2",
        current_amount=Decimal(4.19),
        currency="£",
    )
    c = Items(
        asin="B00OLZXQTM",
        title="item title 3",
        current_amount=Decimal(4.18),
        currency="£",
    )
    add_item(conn, a)
    add_item(conn, b)
    add_item(conn, c)

    # mock alert
    will_1 = Alerts(asin="B07SVVP426", id=1, target_amount=Decimal(6.5))
    will_2 = Alerts(asin="B07G3QKNCQ", id=1, target_amount=Decimal(1.25))
    tom = Alerts(asin="B00OLZXQTM", id=2, target_amount=Decimal(5.24))
    tia = Alerts(asin="B07G3QKNCQ", id=3, target_amount=Decimal(1.85))
    add_alert(conn, will_1)
    add_alert(conn, will_2)
    add_alert(conn, tom)
    add_alert(conn, tia)

    # mock pricehistory
    item1 = Price_History(
        asin="B07SVVP426",
        # title='Natural Magnesium Glycinate 500mg Premium Quality Ideal Strength 100 Vegan Capsules Highest Bioavailability',
        date="2022-01-29",
        amount=9.97,
        currency="£",
    )
    item2 = Price_History(
        asin="B00OLZXQTM",
        # title='Dexam 17819184 Vintage Home Enamelware 400ml Turkish Coffee Pot, Claret Red',
        date="2022-01-29",
        amount=925.0,
        currency="£",
    )
    add_price_history(conn, item1)
    add_price_history(conn, item2)

    return
