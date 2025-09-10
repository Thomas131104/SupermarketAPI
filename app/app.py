# app/app.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.routers import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting API...")
    # setup resource ở đây (DB, cache, file...)
    yield
    print("Shutting down API...")
    # cleanup resource ở đây


app = FastAPI(title="Supermarket Management API",
              version="1.0",
              lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
