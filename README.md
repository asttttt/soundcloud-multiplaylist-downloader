# SoundCloud Playlist Downloader

A [yt-dlp](https://github.com/yt-dlp/yt-dlp) script to downloads multiple SoundCloud playlists as m4a files (AAC, best available quality) with embedded thumbnails and metadata. Each playlist gets its own subfolder with an m3u8 playlist file compatible with VLC, foobar2000 or any playlist-supporting player.
```
SoundCloud_Playlists/
├── Playlist Name/
│   ├── Track 1.m4a
│   ├── Track 2.m4a
│   └── Playlist Name.m3u8
└── Another Playlist/
    ├── Track 1.m4a
    └── Another Playlist.m3u8
```

## Prerequisites

- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp): `pip install yt-dlp`
- [ffmpeg](https://ffmpeg.org/download.html) — must be in PATH

## Adding Playlist URLs

The `PLAYLISTS` section should look like this:
```python
PLAYLISTS = [
    "https://soundcloud.com/user/sets/playlist-one",
    "https://soundcloud.com/user/sets/playlist-two",
    "https://soundcloud.com/user/sets/playlist-three",
]

## Usage

1. Open `downloader.py` and add your SoundCloud playlist URLs to the `PLAYLISTS` list:
```python
PLAYLISTS = [
    "https://soundcloud.com/username/sets/playlist-name",
]
```

2. Run the script:
```
python downloader.py
```
