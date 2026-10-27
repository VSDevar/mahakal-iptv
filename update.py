import re

# The targeted live stream link
YOUTUBE_URL = "https://youtube.com"

def generate_playlist():
    # Force isolate the 11-character video ID from the URL string
    video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', YOUTUBE_URL)
    
    if video_id_match:
        video_id = video_id_match.group(1)
    else:
        # Emergency backup hardcoded ID matching your link if the regex fails
        video_id = "nEJMTbW7N7Y" 
        
    # Standard format that players use to fetch raw YouTube live streams directly
    stream_url = f"https://youtube.com{video_id}"
    
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="MahakalLive" tvg-name="Ujjain Mahakal Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Shri Ujjain Mahakal Live Darshan
{stream_url}
"""
    with open("mahakal.m3u", "w", encoding="utf-8") as file:
        file.write(m3u_template)
    print(f"Success: Playlist written using video ID {video_id}")

if __name__ == "__main__":
    generate_playlist()
