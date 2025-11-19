thonpython
import re

def extract_emails(html: str):
 pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
 emails = re.findall(pattern, html)
 return list(set(emails))