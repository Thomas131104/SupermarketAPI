#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Creating database..."
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"

echo "Starting dev server..."
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
