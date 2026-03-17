import os
import subprocess
import json
from pathlib import Path

PLAYLISTS = [
    # Add your SoundCloud playlist URLs here
    # "https://soundcloud.com/username/sets/playlist-name",
]

def sanitize_name(name):
    invalid = r'<>:"/\|?*'
    return "".join(c if c not in invalid else "_" for c in name)[:100]

def get_playlist_name(url):
    try:
        result = subprocess.run(
            ["yt-dlp", "--dump-json", "--flat-playlist", url],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0 and result.stdout:
            lines = result.stdout.strip().splitlines()
            data = json.loads(lines[0])
            return sanitize_name(data.get('playlist_title') or data.get('title') or url.split("/")[-1])
    except Exception as e:
        print(f"Warning: could not get playlist name: {e}")
    return sanitize_name(url.split("/")[-1])

def download_playlist(url):
    playlist_name = get_playlist_name(url)
    os.makedirs(playlist_name, exist_ok=True)
    print(f"\nDownloading: {playlist_name}")
    subprocess.run([
        "yt-dlp",
        "-f", "bestaudio/best",
        "-x",
        "--audio-format", "m4a",
        "--audio-quality", "0",
        "-o", f"{playlist_name}/%(title)s.%(ext)s",
        "--embed-thumbnail",
        "--embed-metadata",
        url
    ])
    create_m3u8(playlist_name)
    print(f"Done: {playlist_name}")

def create_m3u8(folder):
    m3u8_path = Path(folder) / f"{folder}.m3u8"
    files = sorted([f.name for f in Path(folder).glob("*.*")
                   if f.suffix.lower() in ['.m4a', '.mp3', '.wav', '.flac']])
    with open(m3u8_path, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        f.write("#EXT-X-VERSION:3\n\n")
        for track in files:
            f.write(f"#EXTINF:-1,{track}\n")
            f.write(f"{track}\n\n")

if __name__ == "__main__":
    os.makedirs("SoundCloud_Playlists", exist_ok=True)
    os.chdir("SoundCloud_Playlists")
    print(f"Starting download of {len(PLAYLISTS)} playlists...")
    for i, url in enumerate(PLAYLISTS, 1):
        try:
            print(f"\n[{i}/{len(PLAYLISTS)}]", end=" ")
            download_playlist(url)
        except Exception as e:
            print(f"Error: {e}")
    print("\nAll playlists downloaded!")