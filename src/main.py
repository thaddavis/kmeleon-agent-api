from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from .routers import (
  healthcheck,
  chat,
  auth
)

# from src.db.database import Base, engine

import debugpy

load_dotenv()

# debugpy.listen(("0.0.0.0", 5678))
# debugpy.wait_for_client()

app = FastAPI(docs_url=None, redoc_url=None)

# Base.metadata.create_all(bind=engine)

origins = [
    "https://kalygo.io",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "https://kalygo-nextjs-service-830723611668.us-east1.run.app",
    "https://localhost:3000",
    "http://localhost:5000",  # Second FastAPI
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a Limiter instance
limiter = Limiter(key_func=get_remote_address)

# Add SlowAPI middleware to FastAPI app
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app.include_router(healthcheck.router, prefix="")

app.include_router(
    chat.router,
    prefix="/api",
)

app.include_router(
    auth.router,
    prefix='/api/auth',
    tags=['auth'],
)