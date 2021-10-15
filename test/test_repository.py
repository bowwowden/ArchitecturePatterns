import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from src.adapter.contract_repository import SqlAlchemyRepository
from src.model import Contract
from src.orm import start_mappers, metadata
from src.ports.repository import AbstractRepository


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # engine, which session uses for connection and resources
        engine = create_engine("sqlite:///:memory:", echo=True)
        metadata.create_all(engine)

        # mappers
        start_mappers()

        # create session
        Session = sessionmaker(bind=engine)
        self.session = Session()  # create a Session

    def test_insert_contract(self):
        repo: AbstractRepository() = SqlAlchemyRepository(self.session)

        contract: Contract = Contract(owner_email="william@gmail.com", owner_id=1, contract_id=1)

        repo.create(contract)
        self.session.commit()

        print("Printing the repo return for contract id = 1: \n")

        # Why does this repo read return a None Type?
        repo.read(contract_id=1)


if __name__ == '__main__':
    unittest.main()
