# YouTube Playlist Downloader

This is a Python script that allows you to download videos from a YouTube playlist. It provides three options for downloading videos: download all videos in the playlist at once, download one video at a time, or download a part of the playlist.

## Requirements

- Python 3.6 or higher
- Pytube library

## Installation

1. Clone or download this repository to your local machine.
2. Install Pytube by running `pip install pytube` in your terminal or command prompt.

## Usage

1. Run the `download_youtube_playlist.py` script.
2. Enter the URL of the YouTube playlist when prompted.
3. Select one of the download options: download all videos at once, download one video at a time, or download a part of the playlist.
4. Follow the on-screen instructions to complete the download process.

**Note:** Before running the script, create a folder for the downloaded videos and add the path to the `DOWNLOAD_PATH` variable in the script.

## Example Output

Enter the Youtube Playlist link: https://www.youtube.com/playlist?list=Plolopoplop

- Number of videos in the playlist: 5
- Total duration: 78 minutes 19 seconds
- Total size: 228 MB

How do you want to download the videos?

- Press 1 to download all videos at once.
- Press 2 to download one video at a time.
- Press 3 to download a part of the playlist.

Your choice: 1

- Downloaded: Video 1
- Downloaded: Video 2
- Downloaded: Video 3

Download complete 🎉
