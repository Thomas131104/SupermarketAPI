from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.models.item import ItemTable
from app.schemas.item import ItemBase
from app.schemas.purchase import PurchaseResponse
from app.database import get_db

router = APIRouter()


# Mua hàng
@router.post("/", response_model=PurchaseResponse)
def purchase_item(item_id: int, quantity: int, db: Session = Depends(get_db)):
    item = db.query(ItemTable).filter(ItemTable.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if quantity > item.number:
        raise HTTPException(status_code=400, detail="Not enough stock")

    # Cập nhật số lượng
    item.number -= quantity
    db.commit()
    db.refresh(item)

    # Tính giá cuối cùng (cost x số lượng, áp dụng category discount và tax)
    price_after_discount = item.cost * (1 - item.category.discount / 100)
    total_price = price_after_discount * quantity
    total_price_with_tax = total_price * (1 + item.tax / 100)

    return PurchaseResponse(id=item.id,
                            name=item.name,
                            number=quantity,
                            cost=item.cost,
                            discount=item.category.discount,
                            tax=item.tax,
                            total_price=total_price_with_tax)
