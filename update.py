import urllib.request
import re
import sys

# The verified Channel ID for Krishna Gyan Sagar
CHANNEL_ID = "UC1qqv4R3RhT5OVMy-E_PciQ" 

def get_current_live_id():
    """Extracts the active daily live video ID via public web layouts."""
    try:
        url = f"https://youtube.com{CHANNEL_ID}/live"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode('utf-8')
            
        # Scan page source text directly for the operational watch ID string
        match = re.search(r'\"liveStreamRenderer\":.*?\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html)
        if match:
            return match.group(1)
            
        # Alternate background metadata frame check
        match_fallback = re.search(r'\"videoDescriptionHeaderRenderer\":.*?\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html)
        if match_fallback:
            return match_fallback.group(1)

        # Direct link confirmation backup block
        match_url = re.search(r'\"canonicalBaseUrl\":\"/watch\?v=([a-zA-Z0-9_-]{11})\"', html)
        if match_url:
            return match_url.group(1)
            
        return None
    except Exception as e:
        print(f"Extraction failed: {e}", file=sys.stderr)
        return None

def generate_playlist():
    print("Scanning channel configurations for active stream tag...")
    live_id = get_current_live_id()
    
    if not live_id:
        print("Live ID not found or stream offline. Retaining last active database file.")
        return

    # THE CORRECTED PRIMARY URL AND MULTI-SERVER FAILOVER PATHS
    primary_stream = f"https://kavin.rocks{live_id}"
    backup_stream = f"https://lunar.icu{live_id}"
    
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="KrishnaGyanSagar" tvg-name="Krishna Gyan Sagar Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Krishna Gyan Sagar Live Darshan
{primary_stream}

#EXTINF:-1 tvg-id="KrishnaGyanSagar-Backup" tvg-name="Krishna Gyan Sagar (Backup)" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="2", Krishna Gyan Sagar Live Darshan (Backup)
{backup_stream}
"""
    with open("mahakal.m3u", "w", encoding="utf-8") as file:
        file.write(m3u_template)
    print(f"Sync complete. Compiled operational stream URL: {primary_stream}")

if __name__ == "__main__":
    generate_playlist()
