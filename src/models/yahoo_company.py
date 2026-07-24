from dataclasses import dataclass


@dataclass(slots=True)
class YahooCompany:
    """
    Company metadata returned by Yahoo Finance.
    """

    ticker: str
    name: str
    exchange: str
    currency: str
    quote_type: str
    sector: str | None = None
    industry: str | None = None
    country: str | None = None
    website: str | None = None
