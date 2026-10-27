import sys

# The active video ID string provided by you
LIVE_ID = "6xhkj-qF-cM"

def generate_playlist():
    print(f"Building playlist layout using verified ID: {LIVE_ID}")
    
    # FIXING THE CONCATENATION BY EXPLICITLY ADDING THE PROTOCOL, SUBDOMAIN, AND API PATH
    primary_stream = f"https://kavin.rocks{LIVE_ID}"
    backup_stream = f"https://lunar.icu{LIVE_ID}"
    
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="KrishnaGyanSagar" tvg-name="Krishna Gyan Sagar Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Krishna Gyan Sagar Live Darshan
{primary_stream}

#EXTINF:-1 tvg-id="KrishnaGyanSagar-Backup" tvg-name="Krishna Gyan Sagar (Backup)" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="2", Krishna Gyan Sagar Live Darshan (Backup)
{backup_stream}
"""
    try:
        with open("mahakal.m3u", "w", encoding="utf-8") as file:
            file.write(m3u_template)
        print(f"File generation complete. Correctly set to: {primary_stream}")
    except Exception as e:
        print(f"Failed to write file system data: {e}", file=sys.stderr)

if __name__ == "__main__":
    generate_playlist()
