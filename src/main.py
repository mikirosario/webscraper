from src.utils.scraper import fetch_hn_entries

def main():
    hn_entries = fetch_hn_entries(30)
    for hn_entry in hn_entries:
        print(hn_entry)
    # apply filters and display results

if __name__ == "__main__":
    main()