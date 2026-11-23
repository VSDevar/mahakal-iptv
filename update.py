import subprocess
import sys

# Official verified Ujjain Mahakaleshwar Temple Administration channel ID
CHANNEL_URL = "https://youtube.com"

def get_live_stream_data():
    """Extracts the active live video ID and direct .m3u8 stream URL using yt-dlp."""
    try:
        # Fetch the direct HLS (.m3u8) stream URL and video ID
        cmd = [
            "yt-dlp",
            "--print", "id",
            "--print", "urls",
            "-f", "best[protocol^=m3u8]/best",
            CHANNEL_URL
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            print(f"yt-dlp error: {result.stderr}", file=sys.stderr)
            return None, None
            
        lines = [line.strip() for line in result.stdout.strip().splitlines() if line.strip()]
        if len(lines) >= 2:
            return lines[0], lines[1]
            
        return None, None
    except Exception as e:
        print(f"Extraction failed: {e}", file=sys.stderr)
        return None, None

def generate_playlist():
    print("Scanning temple channel for active live darshan stream...")
    live_id, stream_url = get_live_stream_data()
    
    if not live_id or not stream_url:
        print("Live stream not found or offline. Retaining previous playlist files.")
        return

    logo_url = f"https://ytimg.com{live_id}/hqdefault.jpg"
    
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="MahakalLive" tvg-name="Ujjain Mahakal Live" tvg-logo="{logo_url}" group-title="Devotional;Spiritual" tvg-chno="1", Shri Ujjain Mahakal Live Darshan
{stream_url}
"""
    
    filenames = ["mahakal.m3u", "playlist.m3u", "final.m3u"]
    for name in filenames:
        with open(name, "w", encoding="utf-8") as file:
            file.write(m3u_template)
            
    print(f"Success! Updated playlists with live stream ID ({live_id})")

if __name__ == "__main__":
    generate_playlist()
