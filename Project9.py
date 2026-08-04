import csv
import requests
from bs4 import BeautifulSoup
def scrape_xml(url, news_outlet):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "xml")
    items = soup.find_all("item")
    headlines = []
    for item in items:
        title = item.find("title").text
        link = item.find("link").text
        pub_date_tag = item.find("pubDate")
        pub_date = pub_date_tag.text if pub_date_tag else "Unknown"
        headlines.append({
            "Title": title,
            "Publish Date": pub_date,
            "Link": link,
            "Source": news_outlet}
        )
    return headlines
bbc = scrape_xml("https://feeds.bbci.co.uk/news/rss.xml", "BBC")
print(bbc[2])


