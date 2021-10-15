# This class is essential to mapping the model to the ORM
# Invert the model from the SQL Alchemy model
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import mapper, relationship

from src.model import Contract

metadata = MetaData()

contracts = Table(
    'contracts', metadata,
    Column('contract_id', Integer, primary_key=True, autoincrement=True),
    Column('owner_email', String(255)),
    Column('owner_id', Integer, nullable=False)
)


def start_mappers():
    contracts_mapper = mapper(Contract, contracts)
