from dataclasses import dataclass, field


@dataclass
class Contract:

    contract_id: int
    owner_email: str
    owner_id: int
