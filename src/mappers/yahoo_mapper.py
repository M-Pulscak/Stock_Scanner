from lookups.asset_type_lookup import AssetTypeLookup
from lookups.exchange_lookup import ExchangeLookup

from models.asset import Asset
from models.yahoo_company import YahooCompany


class YahooMapper:

    @staticmethod
    def to_asset(company: YahooCompany) -> Asset:

        return Asset(
            ticker=company.ticker,
            provider_symbol=company.ticker,
            exchange_mic=ExchangeLookup.yahoo_to_mic(company.exchange),
            currency_code=company.currency,
            asset_type=AssetTypeLookup.yahoo_to_asset_type(
                company.quote_type
            ),
            name=company.name,
        )
