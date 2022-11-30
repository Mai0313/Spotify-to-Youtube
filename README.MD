# Spotify to Youtube 
```

This is a simple script that allows you to download a song from Spotify and convert it to a Youtube video.

```

## How to use

* Open https://watsonbox.github.io/exportify/
* Export your playlist in csv (choose whatever you like to export)
* Put those csv inside the data folder
    * Just put it in, it will automatically get all .csv file
* Check https://ytmusicapi.readthedocs.io/en/stable/ to add your cookie info into file name 'headers_auth.json'
* Start main.py, everything will be done soon.
    * Note: The playlist it creates on YouTube Music will be brand new and named as your *.csv name
    * For example, if your csv file is named 'Hello World.csv', the playlist on YouTube Music it creates will be named as 'Hello World'
    
I will make it easiler once I have time
You can use this with some time clock to let it sync automatically


## Tips
```
Processed Song will be recorded in /processed_song separately by csv names with txt format
Failed to find will be recorded in /log together, it won't be too many, so no need to worry
```

## Installation

```py
pip install -r requirements.txt
```

## Usage

```py
python main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## To do list
- [ ] Add a GUI
- [ ] Fix a progress bar
- [x] Add a way to download a playlist
- [ ] Add a way to do Youtube to Spotify
- more to come...

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
[**@Mai0313**](https://github.com/Mai0313/Spotify-to-Youtube)
[**Mai0313**](https://mai0313.com/)

## Dictory tree
```
.
├── README.md
├── main.py
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── spotify.cpython-38.pyc
│   │   └── youtube.cpython-38.pyc
│   ├── spotify.py
│   └── youtube.py
└── test
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   ├── spotify.cpython-38.pyc
    │   └── youtube.cpython-38.pyc
    ├── spotify.py
    └── youtube.py
```
