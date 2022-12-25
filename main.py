import pandas as pd
from ytmusicapi import YTMusic
import time
from tqdm import tqdm
import multiprocessing as mp
import os
from utils.folder_create import create_folder

create_folder()
try:
    ytmusic = YTMusic('headers_auth.json')
except FileNotFoundError:
    print('headers_auth.json file not found..., please check README.md file to get more info')

try:
    filename = [f for f in os.listdir('playlist') if f.endswith('.csv')]
except FileNotFoundError:
    print('playlist csv file not found..., please check README.md file to get more info')

def import_playlist(filename):
    data = (pd.read_csv(f'playlist/{filename}'))[['Track Name', 'Artist Name(s)']].values.tolist()
    # playlist_id = ytmusic.create_playlist(filename[i].replace('.csv', ''), 'created by python script')
    # print(filename[i].replace('.csv', '') + ' has been created')
    progress = tqdm(data, desc='Adding songs to playlist')
    for i in range(len(data)):
        music_name = data[i][0]
        artist_name = data[i][1]
        try:
            search_results = ytmusic.search(music_name + ' ' + artist_name, filter='songs')
            video_id = search_results[0]['videoId']
        # ytmusic.add_playlist_items(playlist_id, [video_id])
        # print(music_name, 'by', artist_name, 'has been added successfully')
        except:
            print(music_name, 'by', artist_name, 'has not been added successfully')
        progress.update(1)
def main():
    filename = [f for f in os.listdir('playlist') if f.endswith('.csv')]
    for i in range(len(filename)):
        import_playlist(filename[i])
        print(filename[i] + ' has been added to youtube music successfully')
if __name__ == '__main__':
    main()