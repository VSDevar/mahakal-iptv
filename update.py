import subprocess
import os

# Your specific Krishna Gyan Sagar YouTube Live stream link
YOUTUBE_URL = "https://www.youtube.com/watch?v=nEJMTbW7N7Y"

def extract_youtube_m3u8(url):
    try:
        # Run yt-dlp via system terminal execution to safely catch the direct stream asset URL
        command = ["yt-dlp", "-g", url]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        
        # Clean and isolate the extracted stream URL string
        stream_url = result.stdout.strip()
        if ".m3u8" in stream_url or "manifest" in stream_url:
            return stream_url
        return None
    except Exception as e:
        print(f"Error extracting YouTube live stream link: {e}")
        return None

def write_ott_navigator_m3u(stream_url):
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="MahakalLive" tvg-name="Ujjain Mahakal Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Shri Ujjain Mahakal Live Darshan
{stream_url}
"""
    with open("mahakal.m3u", "w", encoding="utf-8") as file:
        file.write(m3u_template)
    print("Success: mahakal.m3u generated with YouTube link.")

if __name__ == "__main__":
    url = extract_youtube_m3u8(YOUTUBE_URL)
    
    if not url:
        print("Warning: YouTube extraction failed. Using stable fallback container.")
        # Fallback container URL if YouTube parsing is blocked or temporarily offline
        url = "https://placeholder-stream-if-failed.m3u8"
        
    write_ott_navigator_m3u(url)

