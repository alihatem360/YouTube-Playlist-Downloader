# 🎥 YouTube Playlist Downloader

This Python project allows you to download all videos or a part of them from a YouTube playlist.

## Prerequisites

- Python 3.x installed
- `pytube` library installed (you can install it with `pip install pytube`)



## 🚀 Usage

### watch the video tutorial [here](https://www.loom.com/share/b6b562260e2344988c1e78477a9d30d5?sid=1b64d82a-9656-4907-afcd-37128e0b61b9)
1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you have the `download_youtube_playlist.py` script.

3. Run the script by executing the following command:

   ```bash
   python download_youtube_playlist.py
   ```
 4. The script will prompt you for the following information:
      - Enter the Youtube Playlist link: Enter the URL or ID of the YouTube playlist from which you want to download videos.
      - How do you want to download the videos? Press 1 to download all videos at once.
   5. Press Enter after entering each value.
   6. The script will start downloading the videos from the provided playlist URL. You will see progress messages for each video, such as "Downloading: Video Title" and "Downloaded: Video Title."
   7. Once all downloads are complete, the script will display a "Download Complete" message.

   8. You can find the downloaded videos in the Download directory in the project root.


   ### Note
The part-play-list.py script in the project allows you to download a specific range of videos from a playlist. The usage is similar to download_youtube_playlist.py , but it additionally asks for the start and end video numbers.
