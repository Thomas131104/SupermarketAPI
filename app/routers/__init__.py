from fastapi import APIRouter
from .item import router as item_router
from .category import router as category_router
from .purchase import router as purchase_router
from .stock import router as stock_router

api_router = APIRouter()

api_router.include_router(item_router, prefix="/items", tags=["Items"])

api_router.include_router(category_router,
                          prefix="/categories",
                          tags=["Categories"])

api_router.include_router(purchase_router,
                          prefix="/purchase",
                          tags=["Purchases"])

api_router.include_router(stock_router, prefix="/stock", tags=["Stock"])
