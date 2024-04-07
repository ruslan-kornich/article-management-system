import feedparser


def parse_guardian_rss(url):
    # Parse RSS The Guardian Technology
    feed = feedparser.parse(url)
    for entry in feed.entries:
        tags = [tag['term'] for tag in entry.tags]
        images = [img['url'] for img in entry.media_content]
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Summary: {entry.summary}")
        print(f"Tags: {tags}")
        print(f"Photos: {images}")
        print(f"Publication date: {entry.published}")
        print(f"Author: {entry.author}")
        print("-" * 50)


if __name__ == "__main__":
    rss_url = "https://www.theguardian.com/uk/technology/rss"
    parse_guardian_rss(rss_url)
