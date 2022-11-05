import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from repository.src.adapter.contract_repository import SqlAlchemyRepository
from repository.src.app import App
from repository.src.model import Contract
from repository.src.orm import metadata, start_mappers
from repository.src.ports.repository import AbstractRepository


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.engine = create_engine("sqlite:///:memory:", echo=True)
        metadata.create_all(self.engine)

        # create session
        Session = sessionmaker(bind=self.engine)
        self.session = Session()  # create a Session

        self.repo: AbstractRepository() = SqlAlchemyRepository(self.session)

        # Initialize application using dependency injection
        self.app: App = App(self.repo)

        # mappers
        start_mappers()

    def tearDown(self) -> None:
        metadata.drop_all(self.engine)
        # Wipe all mapped classes between tests
        clear_mappers()

    def test_insert_contract_to_repo(self):
        contract: Contract = Contract(owner_email="william@gmail.com", owner_id=1, contract_id=1)

        self.app.insert_contract(contract)

        print("Contract was created")
        print(self.app.find_contract_by_id(contract_id=1))

        self.assertEqual(self.app.find_contract_by_id(contract_id=1), contract)

    def test_insert_a_list_of_contracts_to_repo(self):
        contract1 = Contract(owner_email="william@gmail.com", owner_id=1, contract_id=1)
        contract2 = Contract(owner_email="frank@gmail.com", owner_id=1, contract_id=2)
        contract3 = Contract(owner_email="bob@gmail.com", owner_id=1, contract_id=3)

        contracts: list = [contract1, contract2, contract3]
        for contract in contracts:
            self.app.insert_contract(contract)

        print("Contract was created")
        print(self.app.find_contract_by_id(contract_id=1))

        self.assertEqual(self.app.contractsRepo.count(), 3)