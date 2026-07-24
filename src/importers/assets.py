from services.yahoo import YahooService
from mappers.yahoo_mapper import YahooMapper
from repositories.asset_repository import AssetRepository
from utils.logger import get_logger


class AssetImporter:
    """
    Imports asset metadata from Yahoo Finance into PostgreSQL.
    """

    def __init__(
        self,
        yahoo_service: YahooService,
        yahoo_mapper: YahooMapper,
        asset_repository: AssetRepository,
    ):
        self._yahoo_service = yahoo_service
        self._yahoo_mapper = yahoo_mapper
        self._asset_repository = asset_repository
        self._logger = get_logger(self.__class__.__name__)

    def import_ticker(self, ticker: str) -> int:
        """
        Imports one ticker.
        Returns:
            asset_id
        """

        self._logger.info("Importing ticker %s", ticker)
        company = self._yahoo_service.get_company_info(ticker)
        asset = self._yahoo_mapper.to_asset(company)
        asset_id = self._asset_repository.upsert(asset)
        self._logger.info(
            "Imported %s (asset_id=%s)",
            ticker,
            asset_id,
        )
        return asset_id

    def import_many(self, tickers: list[str]) -> list[int]:
        asset_ids = []
        total = len(tickers)
        self._logger.info("Starting batch import (%d tickers)", total)
        for index, ticker in enumerate(tickers, start=1):
            self._logger.info("[%d/%d] %s", index, total, ticker)
            asset_ids.append(
                self.import_ticker(ticker)
            )
        self._logger.info("Batch import finished.")
        return asset_ids
