from dataclasses import dataclass


@dataclass
class Contract:

    contract_id: int
    owner_email: str
    owner_id: int
