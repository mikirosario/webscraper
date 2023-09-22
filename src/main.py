from src.models.hn_scraper import HackerNewsScraper

def main():
    scraper = HackerNewsScraper(30)
    for hn_entry in scraper.entries:
        print(hn_entry)
    # apply filters and display results

if __name__ == "__main__":
    main()