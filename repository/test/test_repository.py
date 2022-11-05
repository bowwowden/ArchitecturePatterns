import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from repository.src.adapter.contract_repository import SqlAlchemyRepository
from repository.src.model import Contract
from repository.src.orm import start_mappers, metadata
from repository.src.ports.repository import AbstractRepository


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.engine = create_engine("sqlite:///:memory:", echo=True)
        metadata.create_all(self.engine)

        # create session
        Session = sessionmaker(bind=self.engine)
        self.session = Session()  # create a Session

        self.repo: AbstractRepository() = SqlAlchemyRepository(self.session)

        # mappers
        start_mappers()

    def tearDown(self) -> None:
        clear_mappers()
        metadata.drop_all(self.engine)

    def test_create_contract(self):

        contract: Contract = Contract(owner_email="william@gmail.com", owner_id=1, contract_id=1)

        self.repo.create(contract)

        print("Contract was created")
        print(self.repo.read(contract_id=1))

        self.assertEqual(self.repo.read(contract_id=1), contract)

    def test_create_multiple_contracts(self):
        contract1 = Contract(owner_email="william@gmail.com", owner_id=1, contract_id=1)
        contract2 = Contract(owner_email="frank@gmail.com", owner_id=1, contract_id=2)
        contract3 = Contract(owner_email="bob@gmail.com", owner_id=1, contract_id=3)

        contracts: list = [contract1, contract2, contract3]
        for contract in contracts:
            self.repo.create(contract)

        print("Number of Contracts in the SQL Table " + str(self.repo.count()))

        self.assertEqual(self.repo.count(), 3)

    def test_delete_contract(self):
        contract: Contract = Contract(owner_email="william@gmail.com", owner_id=1, contract_id=1)

        self.repo.create(contract)

        self.repo.delete(contract_id=1)

        assert self.repo.read(contract_id=1) is None

    def test_update_contract(self):
        contract: Contract = Contract(owner_email="william@gmail.com", owner_id=1, contract_id=1)
        self.repo.create(contract)

        self.assertEqual(self.repo.read(contract_id=1), contract)

        new_contract: Contract = Contract(owner_email="williamfbff@gmail.com", owner_id=1, contract_id=1)
        self.repo.update(new_contract)

        self.assertEqual(self.repo.read(contract_id=1), new_contract)


if __name__ == '__main__':
    unittest.main()
