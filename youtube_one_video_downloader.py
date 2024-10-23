from pytubefix import YouTube, exceptions
import os


def download_video(url):
    try:
        yt_video = YouTube(url)
    except exceptions.PytubeError as e:
        print(f"Error initializing video: {e}")
        return

    # الحصول على اسم الفيديو
    video_title = yt_video.title

    # إنشاء مجلد لحفظ الفيديو
    video_folder = "Downloaded_Videos"
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)

    try:
        yt_video.check_availability()
        stream = yt_video.streams.filter(
            progressive=True, file_extension='mp4').get_highest_resolution()
        # Add the title to the video filename
        filename = f"{video_title}.mp4"
        stream.download(output_path=video_folder, filename=filename)
        print(f"Downloaded: {filename}")
    except exceptions.PytubeError as e:
        print(f"Failed to download {yt_video.watch_url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred with {yt_video.watch_url}: {e}")

    print(f"The video has been downloaded successfully in {video_folder}")


if __name__ == "__main__":
    # طلب عنوان URL من المستخدم
    video_url = input("Enter the Youtube Video link: ")

    # تنفيذ دالة التنزيل
    download_video(video_url)
