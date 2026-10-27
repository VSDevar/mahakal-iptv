import urllib.request
import json
import re

# The Channel ID for Krishna Gyan Sagar (UC... format)
# If this ID changes, you can find it in the source code of their YouTube homepage
CHANNEL_ID = "UCzL8t3n2lCjGv83g7m7n5bQ" 

def get_current_live_id():
    """Fetches the active live video ID using a clean web request."""
    try:
        # Requesting the live page HTML directly
        url = f"https://youtube.com{CHANNEL_ID}/live"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode('utf-8')
            
        # Regex search to find the active video ID inside the YouTube page metadata
        match = re.search(r'\"videoDescriptionHeaderRenderer\":\{\"title\":\{\"runs\":\[\{\"text\":\"(.*?)\"\}\].*?\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html)
        if match:
            return match.group(2)
            
        # Fallback regex search if layout differs
        match_fallback = re.search(r'\"canonicalBaseUrl\":\"/watch\?v=([a-zA-Z0-9_-]{11})\"', html)
        if match_fallback:
            return match_fallback.group(1)
            
        return None
    except Exception as e:
        print(f"Error fetching live ID: {e}")
        return None

def generate_playlist():
    print("Fetching the latest active video ID...")
    live_id = get_current_live_id()
    
    if not live_id:
        print("Stream appears to be offline or ID couldn't be parsed. Keeping last working file.")
        return

    # Construct the proxy link using the freshly discovered daily video ID
    stream_url = f"https://kavin.rocks{live_id}"
    
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="KrishnaGyanSagar" tvg-name="Krishna Gyan Sagar Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Krishna Gyan Sagar Live Darshan
{stream_url}
"""
    with open("mahakal.m3u", "w", encoding="utf-8") as file:
        file.write(m3u_template)
    print(f"Success! Playlist updated with fresh daily stream URL: {stream_url}")

if __name__ == "__main__":
    generate_playlist()
