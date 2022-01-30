"""
    Models for SQL tables, for use with psql
"""

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class User:
    email: str
    password: str


@dataclass
class Alert:
    asin: str
    email: str


@dataclass
class Price_History:
    asin: str
    title: str
    date: str
    amount: Decimal
    currency: str
