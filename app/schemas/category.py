from pydantic import BaseModel
from typing import Optional


class CategoryBase(BaseModel):
    """
    Cac cột quan trọng trong bảng Category

    Attributes:
    - name: Loại mặt hàng
    - discount: Discount của loại mặt hàng
    """
    name: str
    discount: float = 0.0


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    discount: Optional[float] = None


class CategoryRead(CategoryBase):
    id: int

    model_config = {"from_attributes": True}


class DiscountUpdate(BaseModel):
    discount: float


class CategoryResponse(BaseModel):
    id: int
    name: str
    discount: float

    model_config = {"from_attributes": True}
