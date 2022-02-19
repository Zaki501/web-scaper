from dataclasses import dataclass
from decimal import Decimal

from werkzeug.security import check_password_hash, generate_password_hash


@dataclass
class User:
    # id: int  # auto increment, primary key
    email: str
    password: str


@dataclass
class Items:
    asin: str  # Primary key
    title: str
    current_amount: Decimal
    currency: str


@dataclass
class Alerts:
    asin: str  # foreign key referencing item.asin
    id: int  # foreign key referencing user.id
    target_amount: Decimal


@dataclass
class Price_History:
    asin: str  # foreign key referencing item.asin
    date: str
    amount: Decimal
    currency: str


if __name__ == "__main__":
    # user registers with password = "password123": store x in db
    x = generate_password_hash("password123")
    y = generate_password_hash("password123")
    print(x)
    print(y)

    # user wants to log in
    # if true,
    #

    print(check_password_hash(x, "password123"))
    print(check_password_hash(y, "password123"))
