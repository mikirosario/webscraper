# webscraper
A simple webscraper written in Python using BeautifulSoup and tested in Python 3.11.2 and 3.10.x.

## Overview
This webscraper extracts the first 30 entries of [Hacker News](https://news.ycombinator.com/), storing each one's title, order, number of comments, and points. It then uses utility functions to filter and sort those entries by these characteristics.

A TDD approach was used for development, starting with the filters and ending with the scraper. A logger has been implemented using the logging module that outputs both to console and to a log file (if there is enough disk space). Entries are encapsulated in a `HackerNewsEntry` object, which features data validation and error handling. The scraper itself along with its filters is
encapsulated in a `HackerNewsScraper` singleton. While not currently used (as only a single fetch is made), a crawl rate limiter is implemented to respect the website's crawl delay.

Python's type hinting is used, as well as runtime type checking.

Automated testing is provided by the pytest module and GitHub Actions.

# Setup and Run
### 1. Clone the Repository
```
git clone https://github.com/yourusername/webscraper.git
cd webscraper
```

### 2. Set Up a Virtual Environment
#### It's recommended to use a virtual environment to avoid conflicts with other projects.
On macOS and Linux:
```
python3 -m venv venv
source venv/bin/activate
```
On Windows:
```
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run Program
```
python -m src.main
```

To run tests:
```
pytest
```
