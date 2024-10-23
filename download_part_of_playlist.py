from pytubefix import Playlist, exceptions
import os


def download_part_of_playlist(url, start_index, end_index):
    try:
        yt_playlist = Playlist(url)
    except exceptions.PytubeError as e:
        print(f"Error initializing playlist: {e}")
        return

    # الحصول على اسم القائمة التشغيل
    playlist_title = yt_playlist.title

    # إنشاء مجلد لحفظ الفيديو
    video_folder = "Downloaded_Videos"
    playlist_folder = os.path.join(video_folder, playlist_title)
    if not os.path.exists(playlist_folder):
        os.makedirs(playlist_folder)

    videos = yt_playlist.videos[start_index-1:end_index]
    for index, video in enumerate(videos, start=start_index):
        try:
            video.check_availability()
            stream = video.streams.filter(
                progressive=True, file_extension='mp4').get_highest_resolution()
            # Add the index to the video title
            filename = f"{index:02d} - {video.title}.mp4"
            stream.download(output_path=playlist_folder, filename=filename)
            print(f"Downloaded: {filename}")
        except exceptions.PytubeError as e:
            print(f"Failed to download {video.watch_url}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred with {video.watch_url}: {e}")

    print(f"The selected part of the playlist has been downloaded successfully in {
          playlist_folder}")


if __name__ == "__main__":
    # طلب عنوان URL من المستخدم
    playlist_url = input("Enter the Youtube Playlist link: ")
    start_index = int(
        input("Enter the start index of the videos to download: "))
    end_index = int(input("Enter the end index of the videos to download: "))

    # تنفيذ دالة التنزيل
    download_part_of_playlist(playlist_url, start_index, end_index)
