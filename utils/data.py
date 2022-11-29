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

def readtxt(filename):
    total = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            processed = f.readlines()
        for i in processed:
            total.append(i.split('\n')[0])
    except:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(filename) + '\n')
    return total

def hashmap(data):
    hashdata = hashlib.md5((data[['Track Name', 'Artist Name(s)']].to_string().encode('utf-8'))).hexdigest()
    return hashdata