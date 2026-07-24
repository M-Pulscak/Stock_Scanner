from abc import ABC
from db.database import Database


class ReferenceNotFoundError(KeyError):
    """Raised when a reference value is not found in cache."""


class ReferenceRepository(ABC):
    """
    Base class for cached reference tables.
    """

    def __init__(
        self,
        db: Database,
        table: str,
        id_column: str,
        key_column: str,
    ):

        self._items: dict[str, int] = {}
        rows = db.fetch_all(
            f"""
            SELECT
                {id_column},
                {key_column}
            FROM {table}
            """
        )
        for row in rows:
            self._items[str(row[key_column]).strip()] = row[id_column]


    def get_id(self, key: str) -> int:
        key = key.strip()
        try:
            return self._items[key]
        except KeyError as ex:
            raise ReferenceNotFoundError(
                f"Unknown value '{key}'"
            ) from ex
