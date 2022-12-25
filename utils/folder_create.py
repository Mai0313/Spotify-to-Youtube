import os

def create_folder():
    # if not os.path.exists('log'):
    #     os.makedirs('log')
    if not os.path.exists('playlist'):
        os.makedirs('playlist')
    # if not os.path.exists('processed_song'):
    #     os.makedirs('processed_song')