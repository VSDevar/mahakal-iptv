# The targeted live stream ID
VIDEO_ID = "nEJMTbW7N7Y"

def generate_playlist():
    # Constructing a valid web stream path for media players
    stream_url = f"https://www.youtube.com/watch?v={VIDEO_ID}"
    
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="MahakalLive" tvg-name="Ujjain Mahakal Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Shri Ujjain Mahakal Live Darshan
{stream_url}
"""
    with open("mahakal.m3u", "w", encoding="utf-8") as file:
        file.write(m3u_template)
    print(f"Success: Playlist written using video URL {stream_url}")

if __name__ == "__main__":
    generate_playlist()
