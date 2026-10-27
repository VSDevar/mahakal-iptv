import sys

# The active video ID string provided by you
LIVE_ID = "6xhkj-qF-cM"

def generate_playlist():
    print(f"Building playlist layout using verified ID: {LIVE_ID}")
    
    # Fully corrected paths including subdomains and live paths
    primary_stream = f"https://kavin.rocks{LIVE_ID}"
    backup_stream = f"https://lunar.icu{LIVE_ID}"
    
    m3u_template = f"""#EXTM3U
#EXTINF:-1 tvg-id="KrishnaGyanSagar" tvg-name="Krishna Gyan Sagar Live" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="1", Krishna Gyan Sagar Live Darshan
{primary_stream}

#EXTINF:-1 tvg-id="KrishnaGyanSagar-Backup" tvg-name="Krishna Gyan Sagar (Backup)" tvg-logo="https://utsav.gov.in" group-title="Devotional;Spiritual" tvg-chno="2", Krishna Gyan Sagar Live Darshan (Backup)
{backup_stream}
"""
    
    # We will write to both common names to ensure the script updates your active playlist file
    filenames = ["mahakal.m3u", "final.m3u", "playlist.m3u"]
    
    for name in filenames:
        try:
            with open(name, "w", encoding="utf-8") as file:
                file.write(m3u_template)
            print(f"Successfully generated playlist target: {name}")
        except Exception as e:
            print(f"Could not write to {name}: {e}", file=sys.stderr)

if __name__ == "__main__":
    generate_playlist()
