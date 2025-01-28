from fastapi import FastAPI, Header, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware
from collections import defaultdict
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones
from lastFM import lastFMAPI
import config
import requests
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods=["GET"],
    allow_headers=["*"]
)

lastfm = lastFMAPI(
    api_key=config.lastFM_key,
    api_secret=config.lastFM_secret,
)

@app.get('/')
async def root(request: Request):
    return {'message' : 'hello'}

@app.get('/lastfm/user/info/{username}')
async def lastfm_user_info(username: str):
    try: 
        user_info = lastfm.get_user_info(username)
        return {'user_info' : user_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/lastfm/top-artist/{username}/{period}')
async def lastfm_top_artists(username: str, period: str):
    try: 
        top_artists = lastfm.get_top_artists(username, period)
        return {'top_artists' : top_artists}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/lastfm/weekly-chart/{username}')
async def lastfm_weekly_chart(username: str):
    try: 
        weekly_chart = lastfm.get_weekly_chart(username)
        return {'weekly_chart' : weekly_chart}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get('/callback/spotify')
async def callback(request: Request):
    pass


@app.get('/auth/lastfm')
async def auth_lastfm():
    callback_url = "http://127.0.0.1:8000/callback/lastfm"
    auth_url = lastfm.get_auth_url(callback_url)
    return {'auth_url' : auth_url}


@app.get('/callback/lastfm')
async def callback(request: Request):
    token = request.query_params.get("token")
    if not token: 
        return {'error' : "No token provided"}
    try:
        session_data = lastfm.create_session(token)
        return {"message" : "Session created", "data" : session_data}
    except Exception as e:
        return {"error" : str(e)}
    