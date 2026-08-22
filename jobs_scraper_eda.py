import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://realpython.github.io/fake-jobs/")
soup = BeautifulSoup(response.text, "html.parser")
jobs = soup.find_all("div", class_="card-content")

jobs_listed = []
for job in jobs:
    # select_one() with a CSS selector (e.g. "h2.title.is-5") is used instead
    # of find() here because these elements have multi-word class attributes
    # (class="title is-5") - find(class_="title is-5") looks for that exact
    # combined string rather than matching both classes independently, so it
    # doesn't reliably work for multi-class elements.
    title = job.select_one("h2.title.is-5").text.strip()
    company = job.select_one("h3.subtitle.is-6.company").text.strip()
    location = job.find("p", class_="location").text.strip()
    # ["datetime"] pulls the attribute's value directly as a string, so no
    # .text is needed afterward - it isn't a tag anymore at that point.
    date_posted = job.find("time")["datetime"]
    jobs_listed.append({
        "Job title": title,
        "Company": company,
        "Location": location,
        "Date posted": date_posted
    })

with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Job title", "Company", "Location", "Date posted"])
    writer.writeheader()
    writer.writerows(jobs_listed)

# Light EDA on the scraped data - most common job titles, which companies
# post the most listings, and how locations are distributed.
df = pd.read_csv("jobs.csv")
print(df["Job title"].value_counts())
print(df["Company"].value_counts())
print(df["Location"].value_counts())