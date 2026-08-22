import pandas as pd

# pd.read_html() scans the page for HTML <table> elements and returns each one
# as a DataFrame. Used here instead of BeautifulSoup because the target data
# (Wikipedia's box office chart) is a genuine HTML table, and this handled the
# page's nested sub-tables (franchise breakdowns) far better than manually
# looping through <tr>/<td> elements did.
tables = pd.read_html(
    "https://en.wikipedia.org/wiki/List_of_highest-grossing_films",
    storage_options={"User-Agent": "Mozilla/5.0"}
)
df = tables[0]

# Worldwide gross was stored as text like "$2,923,710,708", and some rows had
# extra letter codes glued to the front (e.g. "F8$1,238,764,765" for The Fate
# of the Furious). Splitting on "$" and keeping only the last piece reliably
# isolates the real number regardless of what prefix came before it - safer
# than stripping all non-digit characters, which corrupted this column the
# first time around by leaving stray digits from prefixes attached to the
# real number.
df["Worldwide gross"] = df["Worldwide gross"].str.split("$").str[-1]
df["Worldwide gross"] = df["Worldwide gross"].str.replace(",", "", regex=False)
df["Worldwide gross"] = df["Worldwide gross"].astype(float)
pd.set_option("display.float_format", "{:.0f}".format)

# Check whether release year relates to how much a film grossed.
print(df["Year"].corr(df["Worldwide gross"]))

"""
Finding 1: There is no meaningful relationship between a film's release year and
its worldwide gross in this dataset (correlation ~0.04). Gross revenue hovers in
a similar range (roughly $1.0-1.5 billion) across most years in the list, with a
few standout years (1997, 2009, 2021) pulling higher. Caveat: this is raw,
non-inflation-adjusted revenue - a dollar in 1997 is worth substantially more
than a dollar today, so this finding says "no relationship in raw dollar terms,"
not necessarily "no relationship in real popularity/attendance terms," which
inflation could be masking.
"""

# Rank and Peak also had embedded codes (e.g. "43JP", "24RK") rather than
# stray prefixes at the start, so str.extract() with a digit-matching regex
# is used instead of str.split() - it pulls out the leading run of digits
# from each value regardless of what letters follow it.
df["Rank"] = df["Rank"].str.extract(r"(\d+)").astype(int)
df["Peak"] = df["Peak"].str.extract(r"(\d+)").astype(int)

# Rank_Drop shows how far each movie has fallen from its all-time peak
# position to its current rank. 0 means still at peak; a larger positive
# number means it has fallen further since its best moment.
df["Rank_Drop"] = df["Rank"] - df["Peak"]
print(df.sort_values("Rank_Drop", ascending=False)[["Title", "Rank", "Peak", "Rank_Drop"]].head())

"""
Finding 2: Box office rankings in this Top 50 list are not stable over time. On
average, a movie has fallen about 14 positions from its all-time peak rank to its
current rank, and the largest drops are dramatic - Pirates of the Caribbean:
Dead Man's Chest peaked at #3 and has fallen to #48; The Lord of the Rings: The
Return of the King peaked at #2 and now sits at #36. This shows that being in
the Top 50 today is not a permanent achievement - most films are gradually
displaced as newer releases outperform them, so a movie's position on this list
is better read as a snapshot in time than a fixed ranking.
"""



