import os
from sqlalchemy import create_engine

import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from insidegrid.routers import ChangesRouter, UsersRouter, ReleasesRouter


app = FastAPI(title='InsideGrid')

app.add_middleware(SessionMiddleware, secret_key='abc123')

app.include_router(ChangesRouter, prefix='/api')
app.include_router(UsersRouter, prefix='/api')
app.include_router(ReleasesRouter, prefix='/api')

def start():
    uvicorn.run("insidegrid.main:app", host="0.0.0.0", port=8000, reload=True)
