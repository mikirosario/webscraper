from src.models.hn_scraper import HackerNewsScraper

def main():
    scraper = HackerNewsScraper(30)
    original_entries = scraper.entries
    scraper.filter_by_min_title_length(5)
    scraper.sort_by_comments()
    print("\nTitles Longer than 5 Words Sorted by Comments\n")
    for hn_entry in scraper.entries:
        print(hn_entry)
    scraper.entries = original_entries
    scraper.filter_by_max_title_length(5)
    scraper.sort_by_points()
    print("\nTitles Shorter than or Equal to 5 Words Sorted by Points\n")
    for hn_entry in scraper.entries:
        print(hn_entry)

if __name__ == "__main__":
    main()