import subprocess
import sys

# The targeted live stream ID
VIDEO_ID = "nEJMTbW7N7Y"

def get_live_m3u8(video_id):
    youtube_url = f"https://youtube.com{video_id}"
    try:
        # Run yt-dlp silently to get only the direct .m3u8 stream URL
        result = subprocess.run(
            ["yt-dlp", "-g", youtube_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        # Grab the first line of output which contains the direct link
        stream_url = result.stdout.strip().split('\n')[0]
        return stream_url
    except subprocess.CalledProcessError as e:
        print(f"Error fetching live stream: {e.stderr.strip()}", file=sys.stderr)
        return None

def generate_playlist():
    print("Extracting live stream token using yt-dlp...")
    stream_url = get_live_m3u8(VIDEO_ID)
    
    if not stream_url:
        print("Failed to extract stream URL. Aborting file rewrite to protect existing data.")
        return

    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="MahakalLive" tvg-name="Ujjain Mahakal Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Shri Ujjain Mahakal Live Darshan
{stream_url}
"""
    with open("mahakal.m3u", "w", encoding="utf-8") as file:
        file.write(m3u_template)
    print("Success: Playlist updated with fresh YouTube live streaming token.")

if __name__ == "__main__":
    generate_playlist()
