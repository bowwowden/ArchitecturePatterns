import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.adapter.contract_repository import SqlAlchemyRepository
from src.model import Contract
from src.orm import start_mappers, metadata
from src.ports.repository import AbstractRepository


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.engine = create_engine("sqlite:///:memory:", echo=True)
        metadata.create_all(self.engine)


        # create session
        Session = sessionmaker(bind=self.engine)
        self.session = Session()  # create a Session

        self.repo: AbstractRepository() = SqlAlchemyRepository(self.session)

    def tearDown(self) -> None:
        metadata.drop_all(self.engine)

    def test_create_contract(self):
        # mappers
        start_mappers()

        contract: Contract = Contract(owner_email="william@gmail.com", owner_id=1, contract_id=1)

        self.repo.create(contract)

        print("Contract was created")
        print(self.repo.read(contract_id=1))

        self.assertEqual(self.repo.read(contract_id=1), contract)

    def test_delete_contract(self):
        contract: Contract = Contract(owner_email="william@gmail.com", owner_id=1, contract_id=1)

        self.repo.create(contract)

        self.repo.delete(contract_id=1)

        assert self.repo.read(contract_id=1) is None

    def test_update_contract(self):
        contract: Contract = Contract(owner_email="william@gmail.com", owner_id=1, contract_id=1)

        self.repo.create(contract)
        self.repo.update(contract)
        new_contract: Contract = Contract(owner_email="williamfbff@gmail.com", owner_id=1, contract_id=1)

        old = self.repo.read(contract_id=1)
        self.assertNotEqual(old, new_contract)


if __name__ == '__main__':
    unittest.main()
