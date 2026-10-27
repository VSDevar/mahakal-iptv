import os
import re
import requests
from bs4 import BeautifulSoup

# Change this to the exact web page URL hosting the Mahakal stream player
TARGET_URL = "https://example-temple-stream-site.com" 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": os.getenv("COOKIE_DATA", "")
}

def extract_stream_url():
    try:
        response = requests.get(TARGET_URL, headers=headers, timeout=20)
        if response.status_code != 200:
            print(f"Website returned status code: {response.status_code}")
            return None
            
        html = response.text
        
        # Look for explicit streaming playlist extensions (.m3u8)
        m3u8_links = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', html)
        if m3u8_links:
            return m3u8_links[0]
            
        soup = BeautifulSoup(html, 'html.parser')
        source_tag = soup.find("source", src=True)
        if source_tag and ".m3u8" in source_tag["src"]:
            return source_tag["src"]
            
        return None
    except Exception as e:
        print(f"Scraping error: {e}")
        return None

def write_ott_navigator_m3u(stream_url):
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="MahakalLive" tvg-name="Ujjain Mahakal Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Shri Ujjain Mahakal Live Darshan
{stream_url}
"""
    with open("mahakal.m3u", "w", encoding="utf-8") as file:
        file.write(m3u_template)
    print("Success: mahakal.m3u generated.")

if __name__ == "__main__":
    url = extract_stream_url()
    
    if not url:
        print("Warning: Live token link not found on target webpage.")
        # Fallback to an empty file or a placeholder so the Git commit doesn't crash
        # Replace the URL below with a backup link if you have one
        url = "https://placeholder-stream-if-failed.m3u8" 
        
    write_ott_navigator_m3u(url)
