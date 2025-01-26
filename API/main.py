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
    allow_methods=["GET"],
    allow_headers=["*"]
)


@app.get('/')
async def root(request: Request):
    return {'message' : 'hello'}


@app.get('/callback/spotify')
async def callback(request: Request):
    pass

@app.get('/callback/lastfm')
async def callback(request: Request):
    pass