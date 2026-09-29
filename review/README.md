# Larry King review

Apple rejected **#ItsMy2Cents** under **Guideline 4.1(a) — Design: Copycats**,
saying the *metadata* "includes content that resembles Larry King without the
necessary authorization."

This folder is a worksheet, not part of the app. Nothing here is published,
and the build robot ignores it. Delete the folder once the decisions are made.

## The file to open

`larry-king-review.csv` — 105 rows, one per flagged quote. Open it in Numbers
or Excel (or just tap it on GitHub). Columns:

| Column | What it is |
| --- | --- |
| `csv_row` | The line number in `source/quotes.csv`, so it can be found again |
| `tier` | 1, 2 or 3 — see below |
| `risk` | Why it was flagged |
| `reason` | Why the suggested action is what it is |
| `quote` | The quote as it stands today |
| `suggested_action` | `DELETE`, `EDIT` or `KEEP` |
| `suggested_text` | The exact replacement, where the action is `EDIT` |
| `your_decision` | **Empty — for the verdict.** Write `delete`, `keep`, or paste different wording |

## The three tiers

**Tier 1 — 34 quotes. Names Larry King outright.** These are the rejection.
Of the 34, **21 need only a name swap** because the reference is just the show
title, and **13 are proposed for deletion** because the real man *is* the joke —
his 80th birthday, his book, his marriages, being his friend or mentor. Those
cannot be de-identified without deleting the gag.

**Tier 2 — 65 quotes. Uses `#kingsthings`.** This matters more than it looks:
`#kingsthings` was Larry King's own hashtag on Twitter, so it is a direct
borrowing even though his name never appears. Every suggested edit simply drops
the hashtag; not one of the jokes depends on it.

**Tier 3 — 6 quotes. Indirect fingerprints.** The suspenders line and the
serial-marriage running gag. Suggested action is `KEEP`, flagged only so the
choice is a choice. These are the ones most worth keeping, and least worth
putting in a screenshot.

## The rename, and why nothing needs inventing

The archive already contains its own name for the character: **BLK**. Christian
used it himself — "a **BLK Live** exclusive", "my pop, **BLK Sr.**", "the future
**Mrs. BLK**", "Best of **BLK**", and at row 4805 the show is already called
*"What's Happening Now With **BLK**"*.

So every tier-1 edit uses the abbreviation that is already in the voice:

- "Black Larry King" → "BLK"
- "What's Happening Now With Black Larry King" → "What's Happening Now With BLK"
- "Black Larry King Live" → "BLK Live"
- A trailing "Larry King" signature → removed

Nothing is being invented, and the character keeps his surname. He is still a
talk-show host called King who says "It's good to be the King" and books guests
"for the full hour". Those 48 quotes are untouched, because they resemble a
genre, not a person.

## What happens after the decisions

Fill in `your_decision`, hand the file back, and the edits get applied to
`source/quotes.csv` in one commit. Then the robot rebuilds `quotes.json` and
readers get it on next open.

Worst case on the numbers: all 13 tier-1 deletions go through and the archive
drops from 6,138 to 6,125 — a fifth of one percent, and far above the build's
5,000-quote safety floor.

## Also in this folder

`app-store-connect.md` — the metadata audit, the draft reply to Apple, and why
"it's parody" is true but will not by itself clear this rejection.
