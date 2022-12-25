from utils.data import *

create_folder()

for i in range(len(filename)):
    playlist_id = ytmusic.create_playlist(filename[i].replace('.csv', ''), 'created by python script')
    print(filename[i].replace('.csv', '') + ' has been created')
    data = (((lambda x: pd.read_csv(os.path.join(path, filename[i])))(filename[i]))[['Track Name', 'Artist Name(s)']]).values.tolist()
    songlist = f'processed_song/{filename[i].replace(".csv", "")}_list.txt'
    processed = readtxt(songlist)
    for j in range(len(data)):
        if data[j][0] in processed:
            print(f'{data[j][0]} has been processed')
            continue
        else:
            search_results = ytmusic.search(data[j][0] + ' ' + data[j][1], filter='songs')
            video_id = search_results[0]['videoId']
            if video_id is not None:
                ytmusic.add_playlist_items(playlist_id, [video_id])
                with open(songlist, 'a+', encoding = 'utf8') as f:
                    f.write(data[j][0] + '\n')
                print(data[j][0] + ' by ' + data[j][1] + ' added')
            elif video_id is None:
                video_id = search_results[1]['videoId']
                ytmusic.add_playlist_items(playlist_id, [video_id])
                with open(songlist, 'a+', encoding = 'utf8') as f:
                    f.write(data[j][0] + '\n')
                print(data[j][0] + ' by ' + data[j][1] + ' added')
            elif video_id is None:
                video_id = search_results[2]['videoId']
                ytmusic.add_playlist_items(playlist_id, [video_id])
                with open(songlist, 'a+', encoding = 'utf8') as f:
                    f.write(data[j][0] + '\n')
                print(data[j][0] + ' by ' + data[j][1] + ' added')
            else:
                print(data[j][0] + ' by ' + data[j][1] + ' not found')
                with open(f'log/not_found_log.txt', 'a', encoding = 'utf8') as f:
                    f.write(str(data[j][0]) + ' ' + str(data[j][1]) + ' not found' + '\n')
print(filename[i] + ' has been added to youtube music')