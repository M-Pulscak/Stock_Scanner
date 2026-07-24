from db.database import Database

from repositories.exchange_repository import ExchangeRepository
from repositories.currency_repository import CurrencyRepository
from repositories.asset_type_repository import AssetTypeRepository
from repositories.asset_repository import AssetRepository

from services.yahoo import YahooService
from mappers.yahoo_mapper import YahooMapper
from importers.assets import AssetImporter


def main():

    with Database() as db:

        exchange_repo = ExchangeRepository(db)
        currency_repo = CurrencyRepository(db)
        asset_type_repo = AssetTypeRepository(db)

        asset_repo = AssetRepository(
            db,
            exchange_repo,
            currency_repo,
            asset_type_repo,
        )

        importer = AssetImporter(
            YahooService(),
            YahooMapper(),
            asset_repo,
        )

        asset_id = importer.import_ticker("MSFT")

        print(f"Imported asset_id = {asset_id}")


if __name__ == "__main__":
    main()
