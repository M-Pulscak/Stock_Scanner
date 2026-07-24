from db.database import Database
from models.asset import Asset
from repositories.asset_type_repository import AssetTypeRepository
from repositories.currency_repository import CurrencyRepository
from repositories.exchange_repository import ExchangeRepository


class AssetRepository:

    def __init__(
        self,
        db: Database,
        exchange_repo: ExchangeRepository,
        currency_repo: CurrencyRepository,
        asset_type_repo: AssetTypeRepository,
    ):
        self._db = db
        self._exchange_repo = exchange_repo
        self._currency_repo = currency_repo
        self._asset_type_repo = asset_type_repo

    def upsert(self, asset: Asset) -> int:

        exchange_id = self._exchange_repo.get_id(asset.exchange_mic)
        currency_id = self._currency_repo.get_id(asset.currency_code)
        asset_type_id = self._asset_type_repo.get_id(asset.asset_type.value)

        sql = """
        INSERT INTO core.assets
        (
            ticker,
            provider_symbol,
            name,
            exchange_id,
            asset_type_id,
            currency_id
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        ON CONFLICT (exchange_id, ticker)
        DO UPDATE
        SET
            provider_symbol = EXCLUDED.provider_symbol,
            name = EXCLUDED.name,
            asset_type_id = EXCLUDED.asset_type_id,
            currency_id = EXCLUDED.currency_id,
            updated_at = NOW()
        RETURNING asset_id;
        """

        row = self._db.execute_returning(
            sql,
            (
                asset.ticker,
                asset.provider_symbol,
                asset.name,
                exchange_id,
                asset_type_id,
                currency_id,
            ),
        )

        if row is None:
            raise RuntimeError("Upsert asset failed.")

        return row["asset_id"]
