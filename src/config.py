from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


# ---------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    port: int
    name: str
    user: str
    password: str


DATABASE = DatabaseConfig(
    host=os.getenv("DB_HOST", ""),
    port=int(os.getenv("DB_PORT", "5432")),
    name=os.getenv("DB_NAME", ""),
    user=os.getenv("DB_USER", ""),
    password=os.getenv("DB_PASSWORD", ""),
)


# ---------------------------------------------------------------------
# Yahoo Finance
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class YahooPriceConfig:
    history_period: str
    auto_adjust: bool
    include_actions: bool


YAHOO_PRICE = YahooPriceConfig(
    history_period="5y",
    auto_adjust=False,
    include_actions=False,
)
