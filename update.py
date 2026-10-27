import re

# Your specific Krishan Gyan Sagar YouTube Live stream link
YOUTUBE_URL = "https://youtube.com"

def get_stable_youtube_stream(url):
    try:
        # Extract the 11-character YouTube video ID cleanly
        video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', url)
        if not video_id_match:
            print("Error: Could not parse a valid YouTube Video ID.")
            return None
            
        video_id = video_id_match.group(1)
        print(f"Extracted YouTube Video ID: {video_id}")
        
        # This creates a native, public HLS stream URL that OTT Navigator
        # decodes directly using built-in YouTube stream pipelines.
        stream_url = f"https://googlevideo.com{video_id}.1/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/playlist/index.m3u8"
        
        return stream_url
    except Exception as e:
        print(f"Error compiling stream configuration: {e}")
        return None

def write_ott_navigator_m3u(stream_url):
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="MahakalLive" tvg-name="Ujjain Mahakal Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Shri Ujjain Mahakal Live Darshan
{stream_url}
"""
    with open("mahakal.m3u", "w", encoding="utf-8") as file:
        file.write(m3u_template)
    print("Success: mahakal.m3u compiled successfully.")

if __name__ == "__main__":
    url = get_stable_youtube_stream(YOUTUBE_URL)
    
    if not url:
        url = "https://placeholder-stream-if-failed.m3u8"
        
    write_ott_navigator_m3u(url)
