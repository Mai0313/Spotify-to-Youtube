from utils.data import *

for k in tqdm(range(100)):
    for i in range(len(filename)):
        # playlist_id = ytmusic.create_playlist(filename[i].replace('.csv', ''), 'created by python script')
        data = (((lambda x: pd.read_csv(os.path.join(path, filename[i])))(filename[i]))[['Track Name', 'Artist Name(s)']]).values.tolist()
        songlist = f'processed_song/{filename[i].replace(".csv", "")}_list.txt'
        processed = readtxt(songlist)
        for j in range(len(data)):
            if data[j][0] not in processed:
                try:
                    search_results = ytmusic.search(data[j][0] + ' ' + data[j][1], filter='songs')
                    video_id = search_results[0]['videoId']
                    # ytmusic.add_playlist_items(playlist_id, [video_id])
                    with open(songlist, 'a+', encoding = 'utf8') as f:
                        f.write(data[j][0] + '\n')
                    print(data[j][0] + ' by ' + data[j][1] + ' added')
                except:
                    print('value error')
                    with open(f'log/error_log.txt', 'a', encoding = 'utf8') as f:
                        f.write(str(data[j][0]) + ' ' + str(data[j][1]) + ' not found' + '\n')
        time.sleep(30)
    print(filename[i] + ' has been added to youtube music')