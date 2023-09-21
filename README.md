# webscraper
A simple webscraper written in Python using BeautifulSoup and tested in Python 3.11.2
and 3.10.x .

# overview
This webscraper extracts the first 30 entries of https://news.ycombinator.com/, storing
each one's title, order, number of comments and points. It then uses utilitary functions
to filter and sort those entries by these characteristics.

A TDD approach was used for development, starting with the filters and ending with the
scraper. A logger has been implemented using the logging module that outputs both to
console and to log file (if there is enough disk space). Entries are encapsulated in a
HackerNewsEntry object, which features data validation and error handling.

Python's type hinting is used, as well as runtime type checking.

While I opted for a procedural implementation of the filters, to avoid unneeded
complexity and improve readability, these can easily be encapsulated in a filter class,
or an eventual parent to the HackerNewsEntry class, and generalized if the scope of the
application were expanded.

Automated testing is provided by the pytest module and GitHub Actions.

