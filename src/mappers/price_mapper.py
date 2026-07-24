from models.price import Price
from models.yahoo_price import YahooPrice


class PriceMapper:
    """
    Maps YahooPrice to internal Price model.
    """

    @staticmethod
    def map(
        asset_id: int,
        yahoo_price: YahooPrice,
    ) -> Price:

        return Price(
            asset_id=asset_id,
            trading_date=yahoo_price.trading_date,
            open=yahoo_price.open,
            high=yahoo_price.high,
            low=yahoo_price.low,
            close=yahoo_price.close,
            adjusted_close=yahoo_price.adjusted_close,
            volume=yahoo_price.volume,
        )
