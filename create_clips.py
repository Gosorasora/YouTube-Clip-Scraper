from scrape_html import get_most_replayed_data
from pytubefix import YouTube
from moviepy import VideoFileClip
import os
import re
import ssl

# SSL 인증서 검증 우회
ssl._create_default_https_context = ssl._create_unverified_context

def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    
    return emoji_pattern.sub(r'', text)

def download_original_video(video_url, video_id):
    yt = YouTube(video_url)
    video_title = yt.title
    video_stream = yt.streams.filter(file_extension='mp4').first()
    video_stream.download(filename='original_video.mp4')
    
    print(f"Video downloaded: {video_title}\n")
    return video_title

def create_video_clips(data, video_title):
    
    if 'mostReplayed' in data:
        timed_marker_decorations = data['mostReplayed'].get('timedMarkerDecorations', [])
        
        if timed_marker_decorations:
            for idx, decoration in enumerate(timed_marker_decorations):
                start_time = decoration.get('visibleTimeRangeStartMillis') / 1000
                end_time = decoration.get('visibleTimeRangeEndMillis') / 1000
                
                print(f"Initiating Moviepy Processes...\n")
                clip = VideoFileClip('original_video.mp4').subclipped(start_time, end_time)
                clean_video_title = remove_emojis(video_title)
                output_file = f'clips/{clean_video_title}_clip_{idx + 1}.mp4'
                clip.write_videofile(output_file, codec='libx264', logger=None)
                clip.close()
            
            os.remove('original_video.mp4')
            print(f"\nClips created for video {idx + 1}\nDeleting original video...\n")
    else:
        print("Failed to fetch video duration. Please check the API key or video ID.")

def main():
    # 여기에 클립을 만들고 싶은 YouTube 동영상 ID들을 입력하세요
    # 예시: "dQw4w9WgXcQ" (https://www.youtube.com/watch?v=dQw4w9WgXcQ 에서 v= 뒤의 부분)
    video_ids = [
        "3iqIXEjTgcc",  # 예시 동영상 ID - 이것을 원하는 ID로 바꾸세요
        # "dQw4w9WgXcQ",  # 추가 동영상이 있으면 이런 식으로 추가
        # "abcd1234567",  # 더 많은 동영상 처리 가능
    ]
    
    for video_id in video_ids:
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video_title = download_original_video(video_url, video_id)
        data = get_most_replayed_data(video_id)
        create_video_clips(data, video_title)
    
    print("\nAll clips created.")

if __name__ == "__main__":
    main()