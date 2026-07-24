from db.database import Database
from repositories.base.reference_repository import ReferenceRepository


class AssetTypeRepository(ReferenceRepository):

    def __init__(self, db: Database):

        super().__init__(
            db=db,
            table="core.asset_types",
            id_column="asset_type_id",
            key_column="name",
        )
 
