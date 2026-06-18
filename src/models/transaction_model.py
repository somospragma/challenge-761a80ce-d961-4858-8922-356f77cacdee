from pydantic import BaseModel

class Transaction(BaseModel):
    id: str
    amount: float
    currency: str
    status: str

    def json(self):
        return self.json()