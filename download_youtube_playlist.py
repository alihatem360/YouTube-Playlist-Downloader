from pytube import Playlist

link = input("Enter the Youtube Playlist link: ")
DOWNLOAD_PATH = "E:\Download\py_Download\Download"
yt_playlist = Playlist(link)

download_option = input('How do you want to download the videos? \n'
                        'Press 1 to download all videos at once. ⚡ \n'
                        'Your choice: ')

if download_option == '1':
    for video in yt_playlist.videos:
        stream = video.streams.filter(type='video', progressive=True, file_extension='mp4').get_highest_resolution()
        stream.download(DOWNLOAD_PATH)
        print("Downloaded: " + video.title)
    print("\nDownload Complete")
else:
    print("Invalid option. Please choose 1.")
