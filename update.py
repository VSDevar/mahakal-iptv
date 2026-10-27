import sys

LIVE_ID = "6xhkj-qF-cM"

def generate_playlist():
    primary_stream = f"https://kavin.rocks{LIVE_ID}"
    backup_stream = f"https://lunar.icu{LIVE_ID}"
    
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="KrishnaGyanSagar" tvg-name="Krishna Gyan Sagar Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Krishna Gyan Sagar Live Darshan
{primary_stream}

#EXTINF:-1 tvg-id="KrishnaGyanSagar-Backup" tvg-name="Krishna Gyan Sagar (Backup)" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="2", Krishna Gyan Sagar Live Darshan (Backup)
{backup_stream}
"""
    # Writing to all variations to overwrite old configurations completely
    filenames = ["mahakal.m3u", "final.m3u", "playlist.m3u"]
    for name in filenames:
        with open(name, "w", encoding="utf-8") as file:
            file.write(m3u_template)

if __name__ == "__main__":
    generate_playlist()
