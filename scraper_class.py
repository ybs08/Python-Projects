import csv
import time
import requests
from bs4 import BeautifulSoup


class Scraper:
    """
    Scrapes headlines from multiple sources into one shared list. Handles
    both RSS/XML feeds and plain HTML pages, since they need different
    parsing logic - each scrape method builds the same dict shape
    (Title, Publish Date, Link, Source) so results from any source can be
    combined and saved together.
    """

    def __init__(self):
        self.all_headlines = []

    def scrape_xml(self, url, news_outlet):
        try:
            response = requests.get(url, timeout=10)
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return []

        soup = BeautifulSoup(response.text, "xml")
        items = soup.find_all("item")
        xml_headlines = []
        for item in items:
            title = item.find("title").text
            link = item.find("link").text
            # Not every item guarantees a pubDate tag, so this falls back to
            # "Unknown" instead of crashing on a missing tag.
            pub_date_tag = item.find("pubDate")
            pub_date = pub_date_tag.text if pub_date_tag else "Unknown"
            headline = {
                "Title": title,
                "Publish Date": pub_date,
                "Link": link,
                "Source": news_outlet
            }
            xml_headlines.append(headline)
            self.all_headlines.append(headline)
        return xml_headlines

    def scrape_hacker_news(self, url, news_outlet="Hacker News"):
        try:
            response = requests.get(url, timeout=10)
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("span", class_="titleline")
        html_headlines = []
        for item in items:
            link_tag = item.find("a")
            headline = {
                "Title": link_tag.text,
                "Publish Date": "Unknown",  # not available on the HN listing page
                "Link": link_tag["href"],
                "Source": news_outlet
            }
            html_headlines.append(headline)
            self.all_headlines.append(headline)
        return html_headlines

    def get_all_headlines(self):
        return self.all_headlines

    def save_to_csv(self, filename):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Title", "Publish Date", "Link", "Source"])
            writer.writeheader()
            writer.writerows(self.all_headlines)


scraper = Scraper()

# time.sleep() between requests paces the calls out rather than firing them
# rapidly back to back - lower chance of being rate-limited/blocked, and
# more considerate of the servers being hit.
scraper.scrape_xml("https://feeds.bbci.co.uk/news/rss.xml", "BBC")
time.sleep(1)
scraper.scrape_xml("http://rss.cnn.com/rss/cnn_topstories.rss", "CNN")
time.sleep(1)
scraper.scrape_hacker_news("https://news.ycombinator.com")

print(len(scraper.get_all_headlines()))
scraper.save_to_csv("all_headlines.csv")


