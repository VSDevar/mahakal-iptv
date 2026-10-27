import os
import subprocess
import re

# Configured directly for the Krishna Gyan Sagar Channel
YOUTUBE_CHANNEL_URL = "https://youtube.com" 

def get_live_m3u8(channel_url):
    try:
        # Added --cookies flag to bypass YouTube datacenter blocks using your browser session
        result = subprocess.run(
            [
                "yt-dlp", 
                "-g", 
                "-f", "best", 
                "--cookies", "youtube-cookies.txt",
                "--extractor-args", "youtube:player-client=android,web_embedded",
                "-S", "proto:https",
                f"{channel_url}/live"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error extracting stream: {e}")
        if hasattr(e, 'stderr') and e.stderr:
            print(f"Details: {e.stderr}")
        return None

def generate_m3u(stream_url):
    m3u_content = (
        "#EXTM3U refresh=\"180\"\n"
        '#EXTINF:-1 tvg-id="KrishnaGyanSagarMahakal" tvg-name="Mahakal Live (KGS)" tvg-logo="https://mp.gov.in" group-title="Religious Live" tvg-chno="1",Ujjain Mahakal Live (Krishna Gyan Sagar)\n'
        f"{stream_url}\n"
    )
    
    with open("mahakal.m3u", "w", encoding="utf-8") as file:
        file.write(m3u_content)
    print("M3U playlist generated successfully using authentication.")

if __name__ == "__main__":
    live_url = get_live_m3u8(YOUTUBE_CHANNEL_URL)
    if live_url:
        generate_m3u(live_url)
    else:
        print("Failed to fetch active stream URL.")
        exit(1) 
