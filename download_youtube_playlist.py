from pytube import Playlist
import os

link = input("Enter the Youtube Playlist link: ")
DOWNLOAD_PATH = "./Download"
yt_playlist = Playlist(link)

# Create a new folder with the playlist title inside the Download folder
folder_name = yt_playlist.title.replace(
    " ", "_")  # Replace spaces with underscores
folder_path = os.path.join(DOWNLOAD_PATH, folder_name)

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

download_option = input('How do you want to download the videos? \n'
                        'Press 1 to download all videos at once. ⚡ \n'
                        'Your choice: ')

if download_option == '1':
    for video in yt_playlist.videos:
        stream = video.streams.filter(
            type='video', progressive=True, file_extension='mp4').get_highest_resolution()
        stream.download(folder_path)  # Download into the new folder
        print("Downloaded: " + video.title)
    print("\nDownload Complete ✨🔥")
else:
    print("Invalid option. Please choose 1. ⚡")
