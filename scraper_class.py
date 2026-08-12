import csv
import requests
from bs4 import BeautifulSoup
class Scraper:
    def __init__(self):
        self.all_headlines = []
    def scrape_hacker_news(self,url ,  news_outlet="Hacker News"):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("span", class_="titleline")
        html_headlines = []
        for item in items:
            title = item.find("a").text
            link = item.find("a")["href"]
            headline = {
                "Title": title,
                "Publish Date": "Unknown",
                "Link": link,
                "Source": news_outlet
            }
            html_headlines.append(headline)
            self.all_headlines.append(headline)
        return html_headlines

            
        
    def scrape_xml(self, url, news_outlet):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "xml")
        items = soup.find_all("item")
        xml_headlines = []
        for item in items:
            title = item.find("title").text
            link = item.find("link").text
            pub_date_tag = item.find("pubDate")
            pub_date = pub_date_tag.text if pub_date_tag else "Unknown"
            headline = {
                "Title": title,
                "Publish Date": pub_date,
                "Link": link,
                "Source": news_outlet}
            xml_headlines.append(headline)
            self.all_headlines.append(headline)
        return xml_headlines
    def get_all_headlines(self):
        return self.all_headlines
    def save_to_csv(self, filename):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Title", "Publish Date", "Link", "Source"])
            writer.writeheader()
            writer.writerows(self.all_headlines)




