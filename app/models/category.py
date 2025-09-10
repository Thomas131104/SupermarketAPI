from typing import List

from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.database import Base


class CategoryTable(Base):
    __tablename__ = "category"
    __table_args__ = {"comment": "Bảng các thể loại"}
    """
    Các cột trong bảng Category
    
    Attribute:
    - id: ID của loại mặt hàng
    - name: Tên của loại mặt hàng
    - discount: Khuyến mãi loại mặt hàng
    """

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    discount: Mapped[float] = mapped_column(nullable=False, default=0)

    items: Mapped[List["ItemTable"]] = relationship("ItemTable",
                                                    back_populates="category",
                                                    uselist=True)

    model_config = {"from_attributes": True}
