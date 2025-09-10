from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    """
    Cac cột quan trọng trong bảng Item

    Attributes:
    - name: tên của item
    - number: số lượng của item
    - cost: giá của item
    - tax: thuế của item
    - discount: giảm giá của item
    - category_id: id của category mà item thuộc về
    """
    name: str
    number: int
    cost: float
    tax: float
    category_id: int


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int

    model_config = {"from_attributes": True}


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    number: Optional[int] = None
    cost: Optional[float] = None
    tax: Optional[float] = None
    category_id: Optional[int] = None
