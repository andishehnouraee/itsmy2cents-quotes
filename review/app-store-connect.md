# Clearing the 4.1(a) rejection

## What Apple actually objected to

The notice says **metadata**, and that word is doing a lot of work. In App Store
Connect, "metadata" is the store listing, not the app:

- App Name and Subtitle
- Promotional Text, Description, Keywords
- **Screenshots and App Previews**
- What's New
- Support URL and Marketing URL
- The App Store icon
- The notes in App Review Information

The quotes inside the app are *content*, which Apple polices under different
guidelines. So the rejection is almost certainly pointing at something a
reviewer could read on the product page — and the most likely candidate by far
is **a screenshot showing a quote that said "Black Larry King" or `#kingsthings`**.

That is the thing to find first. Before changing anything else, open the build
in App Store Connect and read all six or ten screenshots at full size.

## Why "it's parody, and none of the quotes are real" does not clear it

Both of those things are true, and neither is the argument that gets this
approved. Three reasons:

**Apple is a distributor, not a court.** Parody and satire are defences that get
weighed by a judge against a claim. App Review does not weigh defences. Guideline
4.1 asks a much blunter question: does the listing trade on somebody else's
identity, and is there authorization? "It's a joke" is not authorization, and
review has no mechanism to accept it as one.

**The guideline is aimed at exactly this shape.** 4.1(a) exists for apps built on
a real, named person or brand. Being unmistakably a parody makes the resemblance
*more* legible to a reviewer, not less — the clearer the parody, the clearer the
target. The rejection is evidence a human already made that connection.

**Labelling the app as parody addresses confusion, not appropriation.** A
disclaimer answers "might a user think this is official?" It does not answer
"do you have the right to use his name commercially?" Those are separate
objections, and 4.1(a) is the second one.

The practical read: an argument is a slow loop with an uncertain ending, and a
revision is a fast one with a predictable ending. Revise.

## The metadata audit

Work down this list in App Store Connect. For each field, remove any reference
to Larry King, `#kingsthings`, CNN, or "Black Larry King" / "White Larry King".

- [ ] **App Name** — confirm it is just `#ItsMy2Cents` with no King reference
- [ ] **Subtitle** — 30 chars; a phrase like "Black Larry King's 2 cents" is a direct hit
- [ ] **Keywords** — the easiest field to forget. Any `larry`, `king`, `larry king`, `cnn`, `kingsthings` term must go. Reviewers do read this field even though users never see it
- [ ] **Description** — check the premise paragraph especially; explaining the joke usually means naming him
- [ ] **Promotional Text** — often written in a hurry and then forgotten
- [ ] **What's New** — carries over between versions
- [ ] **Screenshots** — read every word of displayed quote text, including small type and any caption overlay
- [ ] **App Previews** — if there is a video, scrub it frame by frame
- [ ] **App Store icon** — no likeness, no suspenders-and-desk visual quoting his set
- [ ] **Support / Marketing URL** — the linked page is fair game for review; check the landing page copy too
- [ ] **App Review Information notes** — if a previous note said "parody of Larry King", that note *is* the confession. Rewrite it

## The screenshot hazard, which is the real fix

Here is the structural problem, and it is worth more than any single edit.

If the screenshots are captures of a live random feed, then **the archive is
upstream of the metadata**. With 34 Larry King quotes and 65 `#kingsthings`
quotes in a pool of 6,138, any future screenshot session can reintroduce the
exact violation by chance — roughly a 1-in-62 shot per visible quote, which over
ten screenshots with several quotes each is not a remote risk at all. It is how
this probably happened in the first place.

Two things follow:

**1. Scrubbing the archive is the metadata fix, indirectly.** That is the real
reason to do the work in `larry-king-review.csv`, even though the quotes are
content rather than metadata. It removes the source, so the listing cannot
regress.

**2. Stop screenshotting the random feed.** Pick a small, fixed, boring set of
quotes for captures — no real names at all if possible — and use those every
time. A screenshot is a marketing asset that needs to be deliberate, not a
lottery ticket.

There is a related exposure worth knowing about even though Apple did not raise
it: the archive names real people constantly — **952 quotes** say "the great
[somebody]" and **605** say "my friend [somebody]". Passing satirical references
to public figures are a much weaker target than a persona built on one named
person, so this is not the emergency. But it is another reason the screenshot set
should be chosen rather than sampled.

## Draft reply for Resolution Center

Short, factual, no argument. Send it after the metadata is actually updated and
the new build or new metadata is submitted.

> Hello,
>
> Thank you for the review.
>
> We do not claim any rights to Larry King's name or likeness, and we have
> revised our metadata to remove the third-party references rather than assert
> any authorization.
>
> Specifically, we have:
>
> - removed all references to Larry King from the app name, subtitle, keywords,
>   description and promotional text;
> - replaced the screenshots with new captures that contain no third-party
>   names; and
> - removed the references from the app's own quote content, so they cannot
>   appear in future marketing materials.
>
> #ItsMy2Cents is a collection of original satirical quotes written by Christian
> Boone. The character is an original creation and is not presented as, or named
> after, any real person.
>
> Please let us know if anything further is needed.
>
> Thank you,
> Andisheh Nouraee

Two notes on that text. It opens by **declining** the authorization route on
purpose — Apple offered a choice, and picking one clearly is faster than leaving
it open. And it mentions the parody nature once, briefly, at the end as
background rather than as a defence. Leading with the parody argument invites a
reply that asks for documentation instead of approving.

## What not to do

- **Do not attach "documentary evidence" unless a licence genuinely exists.**
  Larry King died in 2021; the rights sit with his estate. Asserting authorization
  that cannot be produced turns a metadata fix into a credibility problem, and
  those escalate.
- **Do not argue First Amendment or fair use in Resolution Center.** True, and
  the wrong venue. It reads as a refusal to fix and gets escalated to App Review
  Board, which is slower.
- **Do not resubmit with metadata changed but the archive untouched** if the
  screenshots are live captures. See the hazard section — it can regress on its
  own.
- **Do not rename the character to another real person.** The obvious swaps
  (another famous interviewer) land in the same guideline.

## One thing worth a lawyer, not me

Separate from Apple's process: several US states recognise a post-mortem right of
publicity, and California's runs for decades after death. Whether a parody
persona built on a named broadcaster implicates that right is a genuine legal
question, and App Store approval would not resolve it either way. If the app is
meant to earn money over a long period, that is worth twenty minutes of a media
lawyer's time. Removing the name, which is what this rejection is forcing
anyway, also happens to be the cheapest way to make the question moot.
