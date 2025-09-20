from fastapi import FastAPI
import process
import asyncio

from prometheus.routes import router as prometheus_router
from postgres.create_db import create_db
from postgres.connect_db import DatabaseConnection


app = FastAPI(title='Gandoo',
              debug=True,
              root_path='/')


app.include_router(prometheus_router)
#app.include_router(healthcheck_router)


@app.on_event('startup')
async def on_srartup():
    create_db()
    asyncio.create_task(process.start_process())


@app.on_event("shutdown")
async def on_shutdown():
    DatabaseConnection.close_connection()
