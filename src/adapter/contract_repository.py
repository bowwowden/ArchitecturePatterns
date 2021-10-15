# Adapter
from sqlalchemy.orm import Session

from src.model import Contract
from src.ports.repository import AbstractRepository


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session: Session):
        self.session = session

    def create(self, contract):
        self.session.add(contract)

    def read(self, contract_id: int):
        self.session.query(Contract).filter_by(contract_id=contract_id).one()

    def update(self, contract):
        pass

    def destroy(self, contract):
        pass