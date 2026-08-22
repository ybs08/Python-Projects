import csv
import requests
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com"
url = base_url +"/page/1/"
all_quotes = []
while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find("span",class_="text").text
        author = quote.find("small", class_="author").text
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]
        all_quotes.append({
            "text": text,
            "author": author,
            "tags": tags
            })
    next_link = soup.find("li", class_="next")
    if next_link:
        next_href = next_link.find("a")["href"]
        url = base_url + next_href
    else:
        url = None
with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
    writer.writeheader()
    writer.writerows(all_quotes)



    
