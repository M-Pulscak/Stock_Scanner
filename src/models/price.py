from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(slots=True)
class Price:
    """
    Daily OHLCV price.
    """

    asset_id: int
    trading_date: date
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    adjusted_close: Decimal
    volume: int
