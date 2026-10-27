import subprocess
import os

YOUTUBE_URL = "https://youtube.com"

def extract_youtube_m3u8(url):
    try:
        cookie_flag = []
        if os.path.exists("youtube_cookies.txt"):
            cookie_flag = ["--cookies", "youtube_cookies.txt"]
            print("Using authentication cookies for extraction...")
            
        # Key Fixes:
        # 1. "-4" forces IPv4 to prevent GitHub runners from stalling on networking (IPv6)
        # 2. "--abort-on-error" ensures it terminates instantly if YouTube blocks the bot
        # 3. "--skip-download" explicitly tells it NOT to process the stream data blocks
        command = [
            "yt-dlp", 
            "-g", 
            "-4", 
            "--abort-on-error", 
            "--skip-download",
            "--extractor-args", "youtube:player_client=tv_downgraded,web,android_vr"
        ] + cookie_flag + [url]
        
        # Adding a 30-second hard timeout constraint so the step NEVER hangs for 3 minutes again
        result = subprocess.run(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            check=True, 
            timeout=30
        )
        
        stream_url = result.stdout.strip()
        if ".m3u8" in stream_url or "manifest" in stream_url:
            return stream_url
        return None
    except subprocess.TimeoutExpired:
        print("Error: Extraction timed out after 30 seconds.")
        return None
    except Exception as e:
        print(f"Extraction block occurred: {e}")
        return None

def write_ott_navigator_m3u(stream_url):
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="MahakalLive" tvg-name="Ujjain Mahakal Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Shri Ujjain Mahakal Live Darshan
{stream_url}
"""
    with open("mahakal.m3u", "w", encoding="utf-8") as file:
        file.write(m3u_template)
    print("Success: Playlist file successfully written.")

if __name__ == "__main__":
    url = extract_youtube_m3u8(YOUTUBE_URL)
    
    if not url:
        print("Warning: YouTube extraction failed. Storing fallback.")
        url = "https://placeholder-stream-if-failed.m3u8"
        
    write_ott_navigator_m3u(url)
