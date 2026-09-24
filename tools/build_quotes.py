#!/usr/bin/env python3
"""
Turn source/quotes.csv into the quotes.json the app downloads.

Run by hand:
    python3 tools/build_quotes.py

It also runs automatically on GitHub whenever source/quotes.csv changes, so
uploading a new spreadsheet in the browser is enough to publish an update.

The CSV needs one column with a header of "Quote". Everything else is ignored.
"""
import csv, hashlib, html, json, re, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source" / "quotes.csv"
OUTPUT = ROOT / "quotes.json"
MIN_LENGTH = 12
# A published file with fewer quotes than this is treated as a mistake.
# Raise it if the archive grows a lot; never lower it to paper over a bad file.
MIN_EXPECTED = 5000

URL = re.compile(r"https?://\S+|\bt\.co/\S+", re.I)
WHITESPACE = re.compile(r"\s+")


def clean(text: str) -> str:
    return WHITESPACE.sub(" ", html.unescape(text)).strip()


def main() -> int:
    if not SOURCE.exists():
        print(f"missing {SOURCE}", file=sys.stderr)
        return 1

    with SOURCE.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, None)
        rows = [row[0] for row in reader if row and row[0].strip()]

    stats = {"rows": len(rows), "retweets": 0, "replies": 0, "links": 0,
             "tooShort": 0, "duplicates": 0}
    seen, quotes = set(), []
    for raw in rows:
        text = clean(raw)
        if text.startswith("RT "):
            stats["retweets"] += 1; continue
        if text.startswith("@") or text.startswith(".@"):
            stats["replies"] += 1; continue
        if URL.search(text):
            stats["links"] += 1; continue
        if len(text) < MIN_LENGTH:
            stats["tooShort"] += 1; continue
        key = text.lower()
        if key in seen:
            stats["duplicates"] += 1; continue
        seen.add(key)
        quotes.append(text)

    if len(quotes) < MIN_EXPECTED:
        print(f"REFUSING TO PUBLISH: only {len(quotes)} quotes, expected at "
              f"least {MIN_EXPECTED}. The spreadsheet looks truncated.",
              file=sys.stderr)
        return 1

    payload = {
        "formatVersion": 1,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "count": len(quotes),
        "checksum": hashlib.sha256("\n".join(quotes).encode()).hexdigest()[:16],
        "copyright": "Quotes (c) Christian Boone and Andisheh Nouraee. All rights reserved.",
        "quotes": quotes,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=0) + "\n",
                      encoding="utf-8")

    print(f"header:   {header}")
    for key, value in stats.items():
        print(f"{key:>11}: {value}")
    print(f"  published: {len(quotes)} quotes -> {OUTPUT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
