import requests
from bs4 import BeautifulSoup
import pandas as pd 

tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_highest-grossing_films", storage_options={"User-Agent": "Mozilla/5.0"})
df = tables[0]
df["Worldwide gross"] = df["Worldwide gross"].str.split("$").str[-1]
df["Worldwide gross"] = df["Worldwide gross"].str.replace(",", "", regex=False)
df["Worldwide gross"] = df["Worldwide gross"].astype(float)
pd.set_option("display.float_format", "{:.0f}".format)
#print(df["Year"].corr(df["Worldwide gross"]))
"""There is no meaningful relationship between a film's release year and its worldwide
gross in this dataset (correlation ≈ 0.04). Gross revenue hovers in a similar range
(roughly $1.0-1.5 billion) across most years in the list, with a few standout years
(1997, 2009, 2021) pulling higher. Important caveat: this is raw, non-inflation-
adjusted revenue - a dollar in 1997 is worth substantially more than a dollar today,
so this finding says "no relationship in raw dollar terms," not necessarily "no
relationship in real popularity/attendance terms," which inflation could be masking."""
df["Rank"] = df["Rank"].str.extract(r"(\d+)").astype(int)
df["Peak"] = df["Peak"].str.extract(r"(\d+)").astype(int)
df["Rank_Drop"] = df["Rank"] - df["Peak"]
print(df.sort_values("Rank_Drop", ascending=False)[["Title", "Rank", "Peak", "Rank_Drop"]].head())




