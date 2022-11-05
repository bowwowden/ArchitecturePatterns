# Adapter
from sqlalchemy.orm import Session

from repository.src.model import Contract
from repository.src.ports.repository import AbstractRepository


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session: Session):
        self.session = session

    def create(self, contract):
        self.session.add(contract)
        self.session.commit()

    def read(self, contract_id: int):
        return self.session.query(Contract).filter_by(contract_id=contract_id).first()

    def update(self, contract):
        contract_id = contract.contract_id
        updated_contract = self.session.query(Contract).filter_by(contract_id=contract_id).one()
        # mapper for updating the contract
        updated_contract.owner_email = contract.owner_email
        updated_contract.owner_id = contract.owner_id
        self.session.commit()

    def delete(self, contract_id):
        self.session.query(Contract).filter_by(contract_id=contract_id).delete()
        self.session.commit()

    def count(self):
        return self.session.query(Contract).count()