thonpython
import json
import logging
import os
from pathlib import Path

from extractors.email_parser import extract_emails
from extractors.html_cleaner import fetch_and_clean_html
from extractors.filters import apply_filters
from outputs.exporter_csv import export_to_csv
from outputs.validator import validate_lead

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CONFIG_PATH = BASE_DIR / "src" / "config" / "settings.example.json"

def load_settings():
 with open(CONFIG_PATH, "r") as f:
 return json.load(f)

def load_urls():
 urls_file = DATA_DIR / "urls.sample.txt"
 if not urls_file.exists():
 raise FileNotFoundError("URLs file not found.")
 with open(urls_file, "r") as f:
 return [url.strip() for url in f.readlines() if url.strip()]

def run():
 settings = load_settings()
 urls = load_urls()
 results = []

 logging.info(f"Loaded {len(urls)} URLs")

 for url in urls:
 try:
 logging.info(f"Processing URL: {url}")
 html = fetch_and_clean_html(url)
 emails = extract_emails(html)

 lead = {
 "name": None,
 "email": emails[0] if emails else None,
 "phone": None,
 "website": url,
 "location": None,
 "industry": None,
 "source_url": url,
 }

 if not validate_lead(lead):
 logging.warning(f"Invalid or incomplete lead for URL: {url}")
 continue

 lead = apply_filters(lead, settings.get("filters", {}))
 results.append(lead)

 except Exception as e:
 logging.error(f"Failed on {url}: {e}")

 output_path = DATA_DIR / "scraped_output.csv"
 export_to_csv(results, output_path)
 logging.info(f"Exported {len(results)} leads to {output_path}")

if __name__ == "__main__":
 run()