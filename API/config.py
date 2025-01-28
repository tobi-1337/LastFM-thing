from dotenv import load_dotenv
import os

load_dotenv()
lastFM_key = os.getenv('lastfm_KEY')
lastFM_secret = os.getenv('lastfm_SECRET')

spotify_id = os.getenv('spotify_ID')
spotify_secret = os.getenv('spotify_SECRET')

print(f"LastFM_Key: {lastFM_key}\nLastFM_Secret: {lastFM_secret}\nSpotify_ID: {spotify_id}\nSpotify_SECRET: {spotify_secret}\n")