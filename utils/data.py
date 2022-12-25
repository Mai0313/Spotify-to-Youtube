import pandas as pd
from ytmusicapi import YTMusic
import time
from tqdm.auto import tqdm
import os

userpath = r'user_cookies_auth'
ytmusic = YTMusic('headers_auth.json')

path = r'playlist'

filename = [f for f in os.listdir(path) if f.endswith('.csv')]

log_path = r'log'

def hashmap(data):
    hashdata = hashlib.md5((data[['Track Name', 'Artist Name(s)']].to_string().encode('utf-8'))).hexdigest()
    return hashdata

def create_folder():
    if not os.path.exists('log'):
        os.makedirs('log')
    if not os.path.exists('playlist'):
        os.makedirs('playlist')
    if not os.path.exists('processed_song'):
        os.makedirs('processed_song')