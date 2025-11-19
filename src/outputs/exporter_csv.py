thonpython
import csv
from pathlib import Path

def export_to_csv(leads: list, out_path: Path):
 if not leads:
 return

 fieldnames = leads[0].keys()

 with open(out_path, "w", newline="", encoding="utf-8") as f:
 writer = csv.DictWriter(f, fieldnames=fieldnames)
 writer.writeheader()
 for lead in leads:
 writer.writerow(lead)