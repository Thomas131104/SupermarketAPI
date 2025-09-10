import uvicorn
import os
from app.app import app
from app.create_table import create_table

port = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    create_table()

    uvicorn.run("app.app:app", host="0.0.0.0", port=port, reload=True)
