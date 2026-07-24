from db.database import Database
from repositories.base.reference_repository import ReferenceRepository


class ExchangeRepository(ReferenceRepository):

    def __init__(self, db: Database):
        super().__init__(
            db=db,
            table="core.exchanges",
            id_column="exchange_id",
            key_column="mic",
        )
