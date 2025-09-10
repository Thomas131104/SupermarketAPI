# Supermarket Management API

Ứng dụng **FastAPI** quản lý siêu thị, cho phép:  
- Quản lý danh mục mặt hàng (Categories)  
- Quản lý sản phẩm (Items)  
- Nhập hàng vào kho (Stock)  
- Mua hàng và tính giá cuối cùng (Purchase)  

---

## 📁 Cấu trúc project

```
workspace/
├── app/
│   ├── app.py                    # Khởi tạo FastAPI app và include routers
│   ├── create_table.py           # (Nếu còn dùng) script tạo bảng thủ công
│   ├── config/                   # Thư mục chứa config (ví dụ PostgreSQL_CONFIG.json)
│   │   └── POSTGRESQL_CONFIG.json
│   ├── database/                 # Database setup
│   │   ├── __init__.py           # Tạo engine, Base, SessionLocal, get_db
│   │   └── supermarket.db        # SQLite database file
│   ├── models/                   # SQLAlchemy models
│   │   ├── __init__.py           # import CategoryTable, ItemTable
│   │   ├── category.py           # CategoryTable
│   │   └── item.py               # ItemTable
│   ├── routers/                  # FastAPI routers
│   │   ├── __init__.py           # include all routers: item, category, purchase, stock
│   │   ├── item.py               # Router cho items
│   │   ├── category.py           # Router cho categories
│   │   ├── purchase.py           # Router cho mua hàng
│   │   └── stock.py              # Router cho nhập hàng
│   ├── schemas/                  # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── category.py           # CategoryBase, CategoryCreate, CategoryUpdate
│   │   └── item.py               # ItemBase, ItemCreate, ItemUpdate
│   └── __pycache__/
├── main.py                       # Entry point chạy uvicorn
├── requirements.txt              # Thư viện cần cài đặt
├── pyproject.toml
├── setup.sh                       # Script setup môi trường
├── supermarket.db                 # SQLite database (nếu chưa trong app/database)
├── uv.lock
├── README.md
├── test/                          # Chứa notebook hoặc file test
└── __pycache__/

```

---

## ⚙️ Cài đặt

1. Clone project:

```bash
git clone <repo-url>
cd <project-folder>
```

2. Cài dependencies:

```bash
pip install -r requirements.txt
```

3. Tạo database: Có 2 cách thực hiện

- Cách 1: Chạy riêng file app/create_table.py bằng lệnh

```bash
python app/create_table.py
```

- Cách 2: Chạy lệnh dưới đây:

```bash
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

Nếu dùng PostgreSQL, sửa database.py với connection string phù hợp và chạy migration (Alembic).

---

## Chạy ứng dụng

- Cách 1: Chạy file main.py (đã bao gồm chạy database) bằng:

```bash
python main.py
```

- Cách 2: Chạy lệnh sau:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

    - API sẽ chạy tại: http://127.0.0.1:8000
    
    - Swagger UI: http://127.0.0.1:8000/docs

---

## API Endpoints

### Categories

| Method | Endpoint           | Mô tả                 |
| ------ | ------------------ | --------------------- |
| POST   | `/categories/`     | Tạo danh mục mới      |
| GET    | `/categories/`     | Lấy danh sách tất cả  |
| GET    | `/categories/{id}` | Lấy chi tiết category |
| PUT    | `/categories/{id}` | Cập nhật category     |
| DELETE | `/categories/{id}` | Xóa category          |

### Items

| Method | Endpoint      | Mô tả                  |
| ------ | ------------- | ---------------------- |
| POST   | `/items/`     | Thêm sản phẩm mới      |
| GET    | `/items/`     | Lấy danh sách sản phẩm |
| GET    | `/items/{id}` | Lấy chi tiết sản phẩm  |
| PUT    | `/items/{id}` | Cập nhật sản phẩm      |
| DELETE | `/items/{id}` | Xóa sản phẩm           |

### Stock

| Method | Endpoint  | Mô tả                                             |
| ------ | --------- | ------------------------------------------------- |
| POST   | `/stock/` | Nhập hàng, nếu sản phẩm tồn tại thì cộng số lượng |

### Purchase

| Method | Endpoint     | Mô tả                              |
| ------ | ------------ | ---------------------------------- |
| POST   | `/purchase/` | Mua hàng, tính giá cuối cùng + tax |

---

## Test:

- Sử dụng Jupyter Notebook (tests/test_backend.ipynb) hoặc requests trong Python để thử API.

- Chạy bằng lệnh sau:

```python
notebook tests/test_backend.py
```

---

## Lưu ý

- Tax được tính theo phần trăm (%).

- Discount của category sẽ áp dụng khi mua hàng.

- Có thể mở rộng bằng Redis cache hoặc các DB khác (PostgreSQL).

