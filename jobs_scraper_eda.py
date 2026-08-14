import requests
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

response = requests.get("https://realpython.github.io/fake-jobs/")
soup = BeautifulSoup(response.text, "html.parser")
jobs = soup.find_all("div", class_="card-content")
jobs_listed = []
for job in jobs:
    title = job.select_one("h2.title.is-5").text.strip()
    company = job.select_one("h3.subtitle.is-6.company").text.strip()
    location = job.find("p", class_="location").text.strip()
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

df = pd.read_csv("jobs.csv")
print(df["Job title"].value_counts())
print(df["Company"].value_counts())
print(df["Location"].value_counts())