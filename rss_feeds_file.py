import feedparser


def get_rss_feeds():
    links = ["https://techcrunch.com/startups/feed/", "https://medium.com/feed/swlh", "https://news.google.com/rss/search?q=agritech+startups&hl=en-US&gl=US&ceid=US:en"]
    feed = []
    for link in links:
        curr_feed = feedparser.parse(link)
        feed.extend(curr_feed["entries"])
    feed = sorted(feed, key=lambda entry: entry["published_parsed"], reverse=True)
    return feed


if __name__ == "__main__":
    get_rss_feeds()
