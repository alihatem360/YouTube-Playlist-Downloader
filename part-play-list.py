import os
from pytube import YouTube, Playlist

# Function to download a video

def download_video(video, download_path):
    try:
        stream = video.streams.filter(
            type='video', progressive=True, file_extension='mp4').get_highest_resolution()
        stream.download(download_path)
        print("Downloaded:", video.title)
    except Exception as e:
        print(f"Error downloading {video.title}: {str(e)}")


# Input start and end video numbers
start_video = int(input('Enter the start video number: '))
end_video = int(input('Enter the end video number: '))

# Define the download path (customize this as needed)
DOWNLOAD_PATH = "E:\Download\py_Download\Download"


# Create the download directory if it doesn't exist
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

# Enter the URL of the YouTube playlist
playlist_url = input('Enter the URL of the YouTube playlist: ')

# Load the playlist
yt_playlist = Playlist(playlist_url)

# Get the videos within the specified range
videos = yt_playlist.videos[start_video - 1:end_video]

# Initialize variables to keep track of total duration and size
total_duration = 0
total_size = 0

# Download each video and calculate total duration and size
for video in videos:
    download_video(video, DOWNLOAD_PATH)
    total_duration += video.length
    total_size += video.streams.filter(type='video', progressive=True,
                                       file_ext10ension='mp4').get_highest_resolution().filesize

# Print the summary
print('\nNumber of videos in the playlist:', len(videos))
print('Total duration:', total_duration // 60,
      'minutes', total_duration % 60, 'seconds')
print('Total size:', total_size // (1024 * 1024), 'MB\n')

# Print download complete message
print("Download Complete")
