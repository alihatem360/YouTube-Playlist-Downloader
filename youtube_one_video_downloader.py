from pytube import YouTube

link = input("Enter the YouTube video link: ")
DOWNLOAD_PATH = "./Download"  # specify your download path here

yt = YouTube(link)
stream = yt.streams.filter(
    progressive=True, file_extension='mp4').get_highest_resolution()
stream.download(DOWNLOAD_PATH)

print("Downloaded: " + yt.title)
