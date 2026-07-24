import yfinance as yf

from models.yahoo_company import YahooCompany


class YahooService:

    def get_company_info(self, ticker: str) -> YahooCompany:

        info = yf.Ticker(ticker).info

        return YahooCompany(
            ticker=info.get("symbol", ticker),
            name=info.get("longName", ""),
            exchange=info.get("exchange", ""),
            currency=info.get("currency", ""),
            quote_type=info.get("quoteType", ""),
            sector=info.get("sector"),
            industry=info.get("industry"),
            country=info.get("country"),
            website=info.get("website"),
        )
