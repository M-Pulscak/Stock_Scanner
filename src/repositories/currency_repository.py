from db.database import Database
from repositories.base.reference_repository import ReferenceRepository


class CurrencyRepository(ReferenceRepository):

    def __init__(self, db: Database):

        super().__init__(
            db=db,
            table="core.currencies",
            id_column="currency_id",
            key_column="code",
        )
