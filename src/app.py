from src.adapter.contract_repository import SqlAlchemyRepository
from src.model import Contract


class App:
    contractsRepo: SqlAlchemyRepository

    def __init__(self, contractsRepo: SqlAlchemyRepository):
        self.contractsRepo = contractsRepo

    def insert_contract(self, contract: Contract):
        self.contractsRepo.create(contract)

    def find_contract_by_id(self, contract_id: int):
        return self.contractsRepo.read(contract_id)
