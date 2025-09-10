from pydantic import BaseModel


class StockCreate(BaseModel):
    item_id: int
    quantity: int
