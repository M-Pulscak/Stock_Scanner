from dataclasses import dataclass
from models.enums import AssetType


@dataclass(slots=True)
class Asset:
    ticker: str
    provider_symbol: str | None
    exchange_mic: str
    currency_code: str
    asset_type: AssetType
    name: str
