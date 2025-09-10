from app.database import Base, engine
from app.models import category, item


def create_table():
    Base.metadata.create_all(bind=engine)
    print("All tables created!")
