# Larry King review — applied

Apple rejected **#ItsMy2Cents** under **Guideline 4.1(a) — Design: Copycats**,
saying the *metadata* "includes content that resembles Larry King without the
necessary authorization."

**All 107 decisions are made and applied.** This folder is the record of what
changed and why. Nothing here is published, and the build robot ignores it.
It can be deleted once the app is through review.

## What was decided

| Tier | What it was | Decision |
| --- | --- | --- |
| 1 (36) | Named Larry King outright | **23 edited, 13 deleted** |
| 2 (65) | Used `#kingsthings`, his own hashtag | **65 edited** — tag dropped |
| 3 (6) | Indirect fingerprints | **kept, by request** |

The archive went from 6,138 to **6,124** quotes — a fifth of one percent, and
far above the build's 5,000-quote safety floor. Two of those fourteen are the
build's own de-duplication: stripping a hashtag left two pairs identical.

After the change, the corpus contains no instance of `Larry King`,
`#kingsthings`, `Black Larry` or `White Larry`.

## The record

`larry-king-review.csv` — 107 rows. Columns:

| Column | What it is |
| --- | --- |
| `original_row` | The row in `source/quotes.csv` **before** the edits |
| `current_row` | The row **now**, or `(deleted)`. The 13 deletions shifted everything after them, so these differ |
| `tier` | 1, 2 or 3 |
| `risk` | Why it was flagged |
| `reason` | Why the action was what it was |
| `quote` | The quote as it stood before the change |
| `suggested_action` | `DELETE`, `EDIT` or `KEEP` |
| `suggested_text` | The replacement, where it was edited |
| `your_decision` | The verdict: `applied edit`, `applied delete` or `keep` |

## The rename needed nothing invented

The archive already contained its own name for the character: **BLK**. Christian
used it himself — "a **BLK Live** exclusive", "my pop, **BLK Sr.**", "the future
**Mrs. BLK**", "Best of **BLK**" — and one quote already called the show
*"What's Happening Now With **BLK**"*.

So every tier-1 edit used the abbreviation that was already in the voice:

- "Black Larry King" → "BLK"
- "What's Happening Now With Black Larry King" → "What's Happening Now With BLK"
- "Black Larry King Live" → "BLK Live"
- A trailing "Larry King" signature → removed

The character kept his surname. He is still a talk-show host called King who
says "It's good to be the King" and books guests "for the full hour" — 48 quotes
untouched, because they resemble a genre rather than a person.

## The thirteen deletions

These could not be de-identified, because the real man *was* the joke: his 80th
birthday, his book *Why I Love Baseball*, his marriages, being his friend and
mentor, and the gags whose entire punchline was the name. A rewrite would have
left a sentence with nothing funny in it.

## Two quotes the first pass missed

The worksheet originally found rows by searching for the full name, so it could
not see two quotes that referred to the persona by first name only:

- the host's son, called "**Black Larry** the 2nd"
- a guest saying *"I'm not sure what you're talking about, **Larry**."*

Both were caught by a residual scan afterwards and fixed as tier 1. They are the
last two tier-1 rows in the file.

Every other `Larry` still in the archive is a real third party being joked about
in passing — Larry Fishburne, Larry Graham, Larry the Cable Guy, General Larry
Platt. Passing satirical references to public figures are a far weaker target
than a persona built on one named person, so those were left alone.

## Tier 3, kept

Six quotes carry indirect fingerprints — the suspenders collection, and the
serial-marriage running gag. Kept by request. They are the funniest of the
flagged set and the least likely to be read as impersonation on their own.

Worth remembering when capturing screenshots, though: see the hazard section in
`app-store-connect.md`. These are quotes to keep in the app and keep out of the
store listing.

## Still outstanding

The archive is clean, but Apple rejected the **listing**, not the archive. The
metadata audit in `app-store-connect.md` has not been done — the keywords field
and the screenshots in particular. That is the work that actually clears the
rejection.
