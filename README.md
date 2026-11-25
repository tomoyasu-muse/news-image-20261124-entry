# 24 November 2026 — The World in One Day

[![make.fun bounty](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/tomoyasu-muse/news-image-20261124-entry/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/tomoyasu-muse/news-image-20261124-entry/reward.svg)](https://make.fun/bounty/news-image-20261124)

A program that writes one image summing up the world news of
**Tuesday 24 November 2026** to `/output/entry.png`, entered in the
[make.fun bounty "Sum up 24 November's world news in one image"](https://make.fun/bounty/news-image-20261124).

## What the image shows

A newspaper front page with the date **24 NOVEMBER 2026** in extra
large type and five stories, each cross-checked across several news
sources reporting that day:

- About five Russian warplanes entering Korea's air defence zone
  early on Tuesday, approaching Ulleung Island: Seoul scrambles
  jets and issues its first preliminary air-raid alert over a
  possible Russian intrusion, lifted in about three minutes with
  no airspace violation, and summons Moscow's attache
- A Russian dawn strike on Zaporizhzhia killing 2 people and
  wounding 40, four of them children, destroying a home and partly
  demolishing a five-storey apartment block
- Israeli strikes in Gaza killing at least 7 people, including a
  child and police officers, as a meningitis epidemic alert is
  issued after 272 cases in October
- A UN femicide brief published on Tuesday: about 47,000 women and
  girls killed by a partner or relative in 2025, five every hour
- WHO and Ebola responders still trapped on Tuesday, over 48 hours
  on, in a hospital maternity ward in Ituri, DR Congo, amid fighting

A ticker adds China extending its pause on the gallium export ban
to the US to 27 January 2027, US plans for new tariffs on 16
trading partners, and about 175 migrants missing from a boat that
left Senegal, whose navy rescued 974 people on Monday.

## How it works

`entry.png` is drawn by `draw_entry.py` (Python + Pillow) before
submission. `main.py` (Python 3.13, standard library only) copies
that finished image to `/output/entry.png`, so two runs in the
offline grading sandbox always write exactly the same bytes.

Run it locally:

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
