from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.models.category import CategoryTable
from app.schemas.category import CategoryBase, CategoryCreate, CategoryUpdate, DiscountUpdate, CategoryResponse
from app.database import get_db

router = APIRouter()


# -------------------------------
# CREATE category
@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = CategoryTable(name=category.name, discount=category.discount)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


# -------------------------------
# READ all categories
@router.get("/", response_model=List[CategoryBase])
def read_categories(skip: int = 0,
                    limit: int = 100,
                    db: Session = Depends(get_db)):
    categories = db.query(CategoryTable).offset(skip).limit(limit).all()
    return categories


# -------------------------------
# READ category by ID
@router.get("/{category_id}", response_model=CategoryBase)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(CategoryTable).filter(
        CategoryTable.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


# -------------------------------
# UPDATE category
@router.put("/{category_id}", response_model=CategoryBase)
def update_category(category_id: int,
                    category_update: CategoryUpdate,
                    db: Session = Depends(get_db)):
    category = db.query(CategoryTable).filter(
        CategoryTable.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    for var, value in vars(category_update).items():
        if value is not None:
            setattr(category, var, value)

    db.commit()
    db.refresh(category)
    return category


# Giảm giá
@router.patch("/{category_id}/discount", response_model=CategoryBase)
def update_discount(category_id: int,
                    data: DiscountUpdate,
                    db: Session = Depends(get_db)):
    category = db.query(CategoryTable).filter(
        CategoryTable.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category.discount = data.discount
    db.commit()
    db.refresh(category)
    return category


# -------------------------------
# DELETE category
@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(CategoryTable).filter(
        CategoryTable.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category)
    db.commit()
    return {"detail": "Category deleted"}
