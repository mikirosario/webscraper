# webscraper
A simple webscraper written in Python using BeautifulSoup.

# overview
This webscraper extracts the first 30 entries of https://news.ycombinator.com/, storing
each one's title, order, number of comments and points. It then uses utilitary functions
to filter and sort those entries by these characteristics.

A TDD approach was used for development, starting with the filters and ending with the
scraper.

Automated testing is provided by the pytest module and GitHub Actions.


