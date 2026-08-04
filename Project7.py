import csv
import requests
from bs4 import BeautifulSoup
class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url
    def fetch_page(self,url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    def parse_quotes(self, soup):
        quotes_list = []
        quotes = soup.find_all("div", class_="quote")
        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = [tag.text for tag in quote.find_all("a", class_="tag")]
            quotes_list.append({
                "Text": text,
                "Author": author,
                "Tags": tags,
            })
        return quotes_list
    def scrape_all_pages(self):
        url = self.base_url + "/page/1/"
        quotes_list = []
        while url:
            soup = self.fetch_page(url)
            quotes_list.extend(self.parse_quotes(soup))
            next_link = soup.find("li", class_="next")
            if next_link:
                href = next_link.find("a")["href"]
                url = self.base_url + href
            else:
                url = None
        return quotes_list
    def save_to_csv(self,filename, quotes_list):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Text", "Author", "Tags"])
            writer.writeheader()
            writer.writerows(quotes_list)
            
        
            
            


site = Scraper("https://quotes.toscrape.com")
results = site.scrape_all_pages()
print(len(results))
site.save_to_csv("quotes.csv", results)