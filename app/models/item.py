from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base


class ItemTable(Base):
    __tablename__ = "items"
    __table_args__ = {"comment": "Bảng lưu trữ các item"}
    """
    Các cột trong bảng Item
    
    Attributes:
    - id (SERIAL): id của item
    - name (STRING): tên của item
    - number (INTEGER): số lượng của item
    - cost (FLOAT): giá của item
    - tax (FLOAT): thuế của item
    - category_id (INTEGER): id của category mà item thuộc về
    """

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(nullable=False)

    number: Mapped[int] = mapped_column(nullable=False)

    cost: Mapped[float] = mapped_column(nullable=False)

    tax: Mapped[float] = mapped_column(nullable=False)

    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"),
                                             nullable=False)

    category: Mapped["CategoryTable"] = relationship("CategoryTable",
                                                     back_populates="items")

    model_config = {"from_attributes": True}
