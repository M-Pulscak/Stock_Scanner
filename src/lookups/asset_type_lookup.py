from typing import Final

from models.enums import AssetType


class UnknownAssetTypeError(ValueError):
    """Raised when Yahoo quoteType cannot be mapped."""


class AssetTypeLookup:

    _YAHOO_TO_ASSET: Final[dict[str, AssetType]] = {
        "EQUITY": AssetType.STOCK,
        "ETF": AssetType.ETF,
        "INDEX": AssetType.INDEX,
        "CRYPTOCURRENCY": AssetType.CRYPTO,
        "CURRENCY": AssetType.FOREX,
        "MUTUALFUND": AssetType.ETF,
    }

    @classmethod
    def yahoo_to_asset_type(cls, quote_type: str) -> AssetType:

        try:
            return cls._YAHOO_TO_ASSET[quote_type.upper()]
        except KeyError as ex:
            raise UnknownAssetTypeError(
                f"Unknown Yahoo quoteType '{quote_type}'"
            ) from ex
