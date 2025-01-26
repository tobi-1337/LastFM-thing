from fastapi import FastAPI, Header, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware
from collections import defaultdict
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods=["GET"],#endast GET tillåts eftersom vi använder bara GET?
    allow_headers=["*"] # behövs någon mer header? vi har ingen autorisering eller säkerhet så tänker att nej, men osäker?!
)


@app.get('/')
async def root(request: Request):
    return {'message' : 'hello'}

