# #ItsMy2Cents quotes

The quote archive the **#ItsMy2Cents** iPhone app reads. Updating the
spreadsheet here changes what readers see, without shipping a new version of
the app and without waiting for App Store review.

The app is in a separate, private repository. Nothing here is app code.

## How to add or change quotes

1. Open `source/quotes.csv` in this repository on the GitHub website.
2. Click the pencil icon to edit in place, or go up to the `source` folder and
   use **Add file > Upload files** to replace it with a new export.
   - Numbers or Excel: **File > Export To > CSV**.
   - Keep the single column and its `Quote` heading.
3. Commit the change.
4. Wait about a minute. A robot rebuilds `quotes.json` and publishes it.
5. Readers get the new quotes the next time they open the app.

You can do all of this from a phone.

## What the robot does

`tools/build_quotes.py` cleans the spreadsheet before publishing:

- drops retweets, replies and anything containing a link
- drops quotes under 12 characters and exact duplicates
- unescapes `&amp;` and friends, and tidies stray whitespace

It then writes `quotes.json` with a count, a timestamp and a checksum.

## The safety net

The build **refuses to publish** a file with fewer than 5,000 quotes, on the
assumption that a much smaller spreadsheet is a truncated or damaged export
rather than a real edit. If you genuinely intend to cut the archive down, raise
`MIN_EXPECTED` in `tools/build_quotes.py` in the same commit.

The app has its own guard: it ignores a downloaded file that fails to parse or
that looks implausibly small, and keeps using the copy it shipped with. A bad
update should therefore be invisible to readers rather than emptying the app.

Every change is kept in this repository's history, so a mistake can be undone
by reverting the commit.

## The address the app reads

```
https://andishehnouraee.github.io/itsmy2cents-quotes/quotes.json
```

## Copyright

Quotes © Christian Boone and Andisheh Nouraee. All rights reserved. Published
here so the app can read them, not as a grant of permission to reuse them.
