from pytube import Playlist

link = input("Enter the Youtube Playlist link: ")
DOWNLOAD_PATH = "E:\Download\py_Download\Download"
yt_playlist = Playlist(link)

# print("The first 5 video titles are:")
# for video in yt_playlist.videos[:5]:
#     print(video.title + "")

# Calculate total duration and size
total_duration = 0
total_size = 0
for video in yt_playlist.videos:
    total_duration += video.length
    stream = video.streams.filter(type='video', progressive=True, file_extension='mp4').get_highest_resolution()
    total_size += stream.filesize

print('\n' + 'Number of videos in the playlist: ' + str(len(yt_playlist.video_urls)))
print('Total duration: ' + str(total_duration // 60) + ' minutes ' + str(total_duration % 60) + ' seconds')
print('Total size: ' + str(total_size // (1024 * 1024)) + ' MB\n')

download_option = input('How do you want to download the videos? \n'
'Press 1 to download all videos at once. ⚡ \n'
'Press 2 to download one video at a time. 🥱 \n'
'Press 3 to download a part of the playlist. ✨\n'
'Your choice: ')

if download_option == '1':
    for video in yt_playlist.videos:
        stream = video.streams.filter(type='video', progressive=True, file_extension='mp4').get_highest_resolution()
        stream.download(DOWNLOAD_PATH)
        print("Downloaded: " + video.title)
    print("\nDownload Complete")
elif download_option == '2':
    for video in yt_playlist.videos:
        print('Title: ' + video.title)
        print('Duration: ' + str(video.length) + ' seconds')
        print('Views: ' + str(video.views))
        stream = video.streams.filter(type='video', progressive=True, file_extension='mp4').get_highest_resolution()
        print('Size: ' + str(stream.filesize // (1024 * 1024)) + ' MB')
        download = input('Do you want to download this video? (y/n): ')
        if download.lower() == 'y':
            stream.download(DOWNLOAD_PATH)
            print("Downloaded: " + video.title + '\n')
        else:
            print("Skipped: " + video.title + '\n')
    print("\nDownload Complete")
elif download_option == '3':
    start_video = int(input('Enter the start video number: '))
    end_video = int(input('Enter the end video number: '))
    videos = yt_playlist.videos[start_video-1:end_video]
    total_duration = sum([video.length for video in videos])
    total_size = sum([video.streams.filter(type='video', progressive=True, file_extension='mp4').get_highest_resolution().filesize for video in videos])
    print('\n' + 'Number of videos in the playlist: ' + str(len(videos)))
    print('Total duration: ' + str(total_duration // 60) + ' minutes ' + str(total_duration % 60) + ' seconds')
    print('Total size: ' + str(total_size // (1024 * 1024)) + ' MB\n')
    for video in videos:
        stream = video.streams.filter(type='video', progressive=True, file_extension='mp4').get_highest_resolution()
        stream.download(DOWNLOAD_PATH)
        print("Downloaded: " + video.title)
 

    print("\nDownload Complete")
else:
    print("Invalid option. Please choose 1, 2 or 3.")
