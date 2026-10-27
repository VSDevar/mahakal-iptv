import urllib.request
import re
import sys

# The official verified temple administration channel ID
CHANNEL_ID = "UCEUuwXHmHckwmdANSy4c7Sw"

def get_current_live_id():
    """Extracts the active daily live video ID from the temple channel."""
    try:
        url = f"https://www.youtube.com/channel/{CHANNEL_ID}/live"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode('utf-8')
            
        # Scan page source layout text directly for the working stream ID string
        match = re.search(r'\"liveStreamRenderer\":.*?\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html)
        if match:
            return match.group(1)
            
        # Alternate internal background metadata configuration check
        match_fallback = re.search(r'\"videoDescriptionHeaderRenderer\":.*?\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html)
        if match_fallback:
            return match_fallback.group(1)

        # Standard navigation tracking backup layout
        match_url = re.search(r'\"canonicalBaseUrl\":\"/watch\?v=([a-zA-Z0-9_-]{11})\"', html)
        if match_url:
            return match_url.group(1)
            
        return None
    except Exception as e:
        print(f"Extraction failed: {e}", file=sys.stderr)
        return None

def generate_playlist():
    print("Scanning temple system channels for active live darshan link...")
    live_id = get_current_live_id()
    
    if not live_id:
        print("Live stream not found or offline. Retaining previous playlist data to prevent black screens.")
        return

    # Compiling the primary and secondary mirror endpoint locations
    primary_stream = f"https://kavin.rocks{live_id}"
    backup_stream = f"https://lunar.icu{live_id}"
    
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="MahakalLive" tvg-name="Ujjain Mahakal Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Shri Ujjain Mahakal Live Darshan
{primary_stream}

#EXTINF:-1 tvg-id="MahakalLive-Backup" tvg-name="Ujjain Mahakal Live (Backup)" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="2", Shri Ujjain Mahakal Live Darshan (Backup)
{backup_stream}
"""
    
    # Overwrite the output files automatically in your workflow environment
    filenames = ["mahakal.m3u", "playlist.m3u"]
    for name in filenames:
        with open(name, "w", encoding="utf-8") as file:
            file.write(m3u_template)
            
    print(f"Success! Output generated with functional live stream ID ({live_id})")

if __name__ == "__main__":
    generate_playlist()
