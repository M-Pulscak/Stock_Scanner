from decimal import Decimal
import pandas as pd
import yfinance as yf
from config import YAHOO_PRICE
from models.yahoo_price import YahooPrice


class YahooPriceService:
    """
    Downloads historical daily prices from Yahoo Finance.
    """

    def get_history(
        self,
        ticker: str,
    ) -> list[YahooPrice]:

        history = yf.Ticker(ticker).history(
            period=YAHOO_PRICE.history_period,
            auto_adjust=YAHOO_PRICE.auto_adjust,
            actions=YAHOO_PRICE.include_actions,
        )

        if history.empty:
            return []
        history = history.reset_index()
        history = history.rename(
            columns={
                "Date": "TradingDate",
                "Adj Close": "AdjClose",
            }
        )

        prices: list[YahooPrice] = []
        for row in history.to_dict("records"):
            prices.append(
                YahooPrice(
                    trading_date=pd.Timestamp(row["TradingDate"]).date(),
                    open=Decimal(str(row["Open"])),
                    high=Decimal(str(row["High"])),
                    low=Decimal(str(row["Low"])),
                    close=Decimal(str(row["Close"])),
                    adjusted_close=Decimal(str(row["AdjClose"])),
                    volume=int(row["Volume"]),
                )
            )

        return prices
