# routers/item.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.models import ItemTable
from app.schemas import ItemCreate, ItemUpdate, ItemBase
from app.database import get_db

router = APIRouter()


# -------------------------------
# CREATE item
# -------------------------------
@router.post("/", response_model=ItemBase)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = ItemTable(name=item.name,
                        number=item.number,
                        cost=item.cost,
                        tax=item.tax,
                        category_id=item.category_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# -------------------------------
# READ all items
# -------------------------------
@router.get("/", response_model=List[ItemBase])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(ItemTable).offset(skip).limit(limit).all()
    return items


# -------------------------------
# READ item by ID
# -------------------------------
@router.get("/{item_id}", response_model=ItemBase)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemTable).filter(ItemTable.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# -------------------------------
# UPDATE item
# -------------------------------
@router.put("/{item_id}", response_model=ItemBase)
def update_item(item_id: int,
                item_update: ItemUpdate,
                db: Session = Depends(get_db)):
    item = db.query(ItemTable).filter(ItemTable.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    for var, value in vars(item_update).items():
        if value is not None:
            setattr(item, var, value)

    db.commit()
    db.refresh(item)
    return item


# -------------------------------
# DELETE item
# -------------------------------
@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemTable).filter(ItemTable.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"detail": "Item deleted"}
