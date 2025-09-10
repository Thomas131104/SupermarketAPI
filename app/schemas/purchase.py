from pydantic import BaseModel


class PurchaseResponse(BaseModel):
    id: int
    name: str
    number: int
    cost: float
    discount: float
    tax: float
    total_price: float

    model_config = {"from_attributes": True}
