from pathlib import Path
from models.models import HackerNewsEntry

# Platform-indifferent path to the mock yCombinator html file from the local directory
MOCK_HTML_FILE_RELATIVE_PATH = Path("mocks") / "hn_sample.html"

# Number of entries in the mock yCombinator html file
MOCK_HTML_HN_ENTRIES_NUM = 30

# Number of entries to fetch from the mock yCombinator html file
MOCK_HTML_HN_ENTRIES_NUM_TO_FETCH = 20

# Expected
MOCK_HTML_EXPECTED_RETURN_VALUE = [
    HackerNewsEntry('Cisco Acquires Splunk', 1, 189, 363),
    HackerNewsEntry('Nippon Television has just acquired Studio Ghibli', 2, 59, 276),
    HackerNewsEntry('Why Kakoune', 3, 14, 47),
    HackerNewsEntry('They have genetic ALS. What should clinicians do?', 4, 7, 23),
    HackerNewsEntry('OpenBSD/ARM64 on Hetzner Cloud', 5, 97, 168),
    HackerNewsEntry('Launch HN: Loops (YC W22) – Email for SaaS Companies', 6, 43, 50),
    HackerNewsEntry('An INI Critique of TOML (2021)', 7, 62, 84),
    HackerNewsEntry('Intel Xeon Max 9480 Deep-Dive 64GB HBM2e Onboard Like a GPU or AI Accelerator', 8, 38, 77),
    HackerNewsEntry('Call to shut down Bristol schools’ use of app to ‘monitor’ pupils and families', 9, 66, 96),
    HackerNewsEntry('BWXT and Crowley Developing Nuclear Power Generation Ships', 10, 21, 37),
    HackerNewsEntry('The SEC cracks down on greenwashing', 11, 4, 32),
    HackerNewsEntry('Show HN: Odin – the integration of LLMs with Obsidian note taking', 12, 44, 57),
    HackerNewsEntry('Airlines Are Just Banks Now', 13, 110, 120),
    HackerNewsEntry('Issue affecting the Gateway API on the Braintree platform', 14, 56, 124),
    HackerNewsEntry('Strong arrows: a new approach to gradual typing', 15, 37, 112),
    HackerNewsEntry('Fosstodon is now invite only', 16, 33, 21),
    HackerNewsEntry('Why I’m stepping down', 17, 20, 20),
    HackerNewsEntry('Erlang/OTP 26.1 Released', 18, 51, 177),
    HackerNewsEntry('Introduction to Linux interfaces for virtual networking (2018)', 19, 11, 156),
    HackerNewsEntry('Guide to Searching and Annotating Text on Maps', 20, 5, 45)
]