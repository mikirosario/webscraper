# HTTP request header
HN_HTTP_REQUEST_HEADER = {
    "User-Agent": "webscraper (+https://github.com/mikirosario/webscraper)"
    }

# URL for the YCombinator news page
HN_URL = "https://news.ycombinator.com/news"

# HTML tag and class where each entry begins
HN_ENTRY_START_TAG = 'tr'
HN_ENTRY_START_CLASS = 'athing'

# HTML tag where the title can be found
HN_TITLE_TAG = 'span'
# HTML class where the title can be found within the tag
HN_TITLE_CLASS = 'titleline'

# HTML tag where the order_num can be found
HN_ORDER_NUM_TAG = 'span'
# HTML class where the order_num can be found within the tag
HN_ORDER_NUM_CLASS = 'rank'

# HTML tag where the comment_count can be found
HN_COMMENT_COUNT_TAG = 'a'

# HTML tag where the points can be found
HN_POINTS_TAG = 'span'
# HTML class where the points can be found within the tag
HN_POINTS_CLASS = 'score'

# Number of entries to fetch from Hacker News
NUM_HN_ENTRIES = 30

# Log file name
LOG_FILE_NAME = 'log.log'

# Maximum size of a log file
LOG_FILE_MAX_BYTES = 5 * 1024 * 1024  # 5MB

# Maximum number of log files
LOG_FILE_MAX_NUM = 3