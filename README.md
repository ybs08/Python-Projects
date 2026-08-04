# Python Projects

A collection of Python projects built while working through a self-directed learning path toward AI/ML specialization. Covers core OOP, file I/O, web scraping, and exploratory data analysis (EDA).

## Projects

### expense_tracker.py
A command-line expense tracker. Uses classes to represent transactions, supports adding expenses, viewing totals (overall and by category), and saving/loading data to a JSON file so records persist between runs.

**Concepts:** OOP basics, file I/O, JSON serialization, CLI menu loops

---

### inventory_system.py
A library/inventory management system with a base `Item` class and `Book`/`Electronics` subclasses. Supports adding, removing, and searching items, listing the full inventory, and saving/loading the inventory to a JSON file.

**Concepts:** Inheritance, polymorphism, file persistence

---

### text_adventure.py
A small text-based adventure game with multiple connected rooms, an inventory system for the player, and both win and lose conditions based on player choices and health.

**Concepts:** Object state management, command parsing, game loop design

---

### quote_scraper.py
A web scraper that pulls quotes, authors, and tags from [quotes.toscrape.com](https://quotes.toscrape.com), following pagination across every page on the site, and saves the results to a CSV file.

**Concepts:** `requests`, `BeautifulSoup`, HTML parsing, pagination, CSV export

---

### titanic_eda.py
Exploratory data analysis on the classic Titanic dataset. Covers missing-value handling, single-column distributions, and relationships between survival, passenger class, and sex.

**Concepts:** `pandas`, `matplotlib`/`seaborn`, missing data strategies, groupby analysis, correlation

---

### scraper_class.py
A refactor of the quote scraper into a reusable `Scraper` class, with separate methods for fetching a page, parsing quotes, scraping all pages via pagination, and saving results to CSV.

**Concepts:** OOP design applied to a scraping workflow, code reuse

---

### data_cleaner_class.py
A reusable `DataCleaner` class that wraps common EDA cleaning steps — filling missing values (median/mode/mean), dropping columns, filtering rows, and printing a data summary — so the same cleaning logic can be applied across different datasets without rewriting it each time.

**Concepts:** OOP design applied to a data-cleaning workflow, reusable pandas utilities

## Setup

Each script only needs the libraries it uses. Install what's required for the project you want to run:

```bash
pip install pandas matplotlib seaborn requests beautifulsoup4
```

## Notes

These projects were built as a structured refresher/practice series, each one adding a new concept on top of the last — starting from core OOP and file handling, moving into web scraping, and finishing with exploratory data analysis in preparation for further study in machine learning.
