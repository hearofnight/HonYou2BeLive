import os
import sys
import googleapiclient.discovery
import requests

# 设置API密钥
API_KEY = os.environ.get('YOUTUBE_API_KEY')
#API_KEY = "YOUR_YOUTUBE_API_KEY"

def get_live_stream_url(video_id):
    # 创建 YouTube API 客户端
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

    # 获取视频的直播流信息
    request = youtube.videos().list(
        part="liveStreamingDetails",
        id=video_id
    )
    response = request.execute()

    # 提取直播流的 m3u8 URL
    try:
        live_stream_url = response["items"][0]["liveStreamingDetails"]["hlsUrl"]
        return live_stream_url
    except:
        return None

def write_to_m3u8_file(channel_name, live_stream_url):
    with open(f'newchannels/{channel_name}.m3u8', 'w') as f:
        f.write('#EXTM3U\n')
        f.write('#EXT-X-VERSION:3\n')
        f.write(f'#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000\n')
        f.write(f'{live_stream_url}\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 your_script.py <channel_name>")
        sys.exit(1)

    channel_name = sys.argv[1]

    # 从文件中读取视频的 URL
    with open(f'/home/runner/work/HonYou2BeLive/HonYou2BeLive/sources/{channel_name}.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('~~'):
                continue
            if line.startswith('https://www.youtube.com/watch?v='):
                video_id = line.split("=")[-1]
                live_stream_url = get_live_stream_url(video_id)
                if live_stream_url:
                    write_to_m3u8_file(channel_name, live_stream_url)
                else:
                    print(f"Failed to get live stream URL for video ID: {video_id}")
            else:
                print("Invalid URL format:", line)
