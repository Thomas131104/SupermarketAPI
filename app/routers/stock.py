from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.models.item import ItemTable
from app.schemas.item import ItemCreate
from app.schemas.stock import StockCreate
from app.database import get_db

router = APIRouter()


@router.post("/")
def add_stock(stock: StockCreate, db: Session = Depends(get_db)):
    db_item = db.query(ItemTable).filter(ItemTable.id == stock.item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.number += stock.quantity
    db.commit()
    db.refresh(db_item)
    return {"detail": f"Stock updated. Current number: {db_item.number}"}
