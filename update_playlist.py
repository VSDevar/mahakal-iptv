import os
import re
import requests
from bs4 import BeautifulSoup

# Replace this with the actual URL where the Mahakal Live player is embedded
TARGET_URL = "https://www.youtube.com/watch?v=nEJMTbW7N7Y" 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": os.getenv("COOKIE_DATA", "")
}

def extract_stream_url():
    try:
        response = requests.get(TARGET_URL, headers=headers, timeout=20)
        if response.status_code != 200:
            print(f"Failed to load page. Status code: {response.status_code}")
            return None
            
        html = response.text
        
        # Look for direct .m3u8 source links inside the JavaScript or HTML source
        m3u8_links = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', html)
        if m3u8_links:
            # Filters out common layout elements, returns the first match
            return m3u8_links[0]
            
        # Fallback: Look inside standard HTML5 video tags
        soup = BeautifulSoup(html, 'html.parser')
        source_tag = soup.find("source", src=True)
        if source_tag and ".m3u8" in source_tag["src"]:
            return source_tag["src"]
            
        return None
    except Exception as e:
        print(f"Error during extraction parsing: {e}")
        return None

def write_ott_navigator_m3u(stream_url):
    # Formatted with extended attributes optimized for OTT Navigator UI rendering
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="MahakalLive" tvg-name="Ujjain Mahakal Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Shri Ujjain Mahakal Live Darshan
{stream_url}
"""
    with open("mahakal.m3u", "w", encoding="utf-8") as file:
        file.write(m3u_template)
    print("Success: mahakal.m3u updated for OTT Navigator.")

if __name__ == "__main__":
    url = extract_stream_url()
    if url:
        write_ott_navigator_m3u(url)
    else:
        print("Could not find a valid live streaming archive link on the page.")
        # Exiting cleanly prevents GitHub from marking the action as completely failed if the site goes down briefly
        exit(0)
