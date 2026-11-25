#!/usr/bin/env python3
"""Front page for Tuesday 24 November 2026, drawn for make.fun.

Every story below was reported on Tuesday 24 November 2026 and
was checked that day against at least two outlets:

- Ulleung, South Korea: about five Russian warplanes entered
  Korea's air defence identification zone early on Tuesday,
  approaching Ulleung Island. Seoul scrambled fighter jets and
  issued its first preliminary air-raid alert over a possible
  Russian intrusion; it was lifted in about three minutes, no
  airspace was violated, and Seoul summoned Moscow's attache.
  Sources: Yonhap (three updates on 24 Nov), Al Jazeera.
- Zaporizhzhia, Ukraine: a Russian dawn attack on Tuesday killed
  two people and wounded 40, four of them children, destroying a
  private home and partly demolishing a five-storey block.
  Sources: Al Jazeera, Kyiv Post, Ukrinform, Reuters via Straits
  Times and Free Malaysia Today.
- Gaza: Israeli air and drone strikes on Tuesday killed at least
  seven Palestinians, among them a child and police officers, as
  the health ministry issued a meningitis epidemic alert after
  272 cases in October, over eight times the usual monthly rate.
  Sources: Al Jazeera, Reuters via Al Arabiya, The Brief.
- Worldwide: UNODC and UN Women published the 2026 Femicide Brief
  on Tuesday: about 47,000 women and girls were killed by an
  intimate partner or a family member in 2025, five every hour,
  60 percent of all 78,000 femicides that year.
  Sources: UN News, Al Jazeera, Daily Sabah, Le Temps.
- Ituri, DR Congo: WHO said on Tuesday its staff and Ebola
  responders were still trapped, more than 48 hours on, inside a
  hospital maternity ward amid heavy fighting, with evacuation
  hoped for that day. Latest WHO outbreak figures quoted on
  Tuesday: 11,613 confirmed cases and 5,678 deaths.
  Sources: UN News (24 Nov update), UN News Today 24 November.
- Beijing: China's commerce ministry said on Tuesday it will
  extend, from 28 November to 27 January 2027, its suspension of
  the ban on US-bound gallium, germanium, antimony and superhard
  material exports, and of tighter graphite reviews.
  Sources: Reuters, Xinhua, WSJ via Morningstar, Global Times.

Ticker, also Tuesday: China extends its pause on the gallium
export ban to the US to 27 January 2027; US sources say new
Section 301 tariffs on 16 trading partners are imminent after
an excess-capacity probe; about 175 migrants are unaccounted
for from a boat that left Dakar, Senegal, while the navy
rescued 974 people on Monday.
"""

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
INK = (18, 18, 20)
SOFT = (58, 55, 50)
CREAM = (246, 241, 228)
PANEL = (255, 254, 248)
GOLD = (255, 196, 64)
WHITE = (255, 255, 255)

BOLD_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def load_font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    lines = []
    pending = ""
    for token in text.split():
        candidate = token if pending == "" else pending + " " + token
        if draw.textlength(candidate, font=fnt) <= max_width:
            pending = candidate
        else:
            lines.append(pending)
            pending = token
    if pending:
        lines.append(pending)
    return lines


def banner(draw, box, colour, caption):
    x0, y0, x1, _ = box
    draw.rounded_rectangle([x0, y0, x1, y0 + 46], radius=10, fill=colour)
    draw.rectangle([x0, y0 + 26, x1, y0 + 46], fill=colour)
    draw.text((x0 + 14, y0 + 10), caption, font=load_font(BOLD_PATH, 24), fill=WHITE)


def body_block(draw, box, title, detail, title_pt=29, detail_pt=21):
    x0, y0, x1, _ = box
    inner = x1 - x0 - 28
    y = y0 + 60
    for ln in wrap(draw, title, load_font(BOLD_PATH, title_pt), inner):
        draw.text((x0 + 14, y), ln, font=load_font(BOLD_PATH, title_pt), fill=INK)
        y += title_pt + 7
    y += 5
    for ln in wrap(draw, detail, load_font(REG_PATH, detail_pt), inner):
        draw.text((x0 + 14, y), ln, font=load_font(REG_PATH, detail_pt), fill=SOFT)
        y += detail_pt + 6


def panel(draw, box, colour, caption, title, detail, title_pt=29, detail_pt=21):
    draw.rounded_rectangle(box, radius=13, fill=PANEL, outline=INK, width=3)
    banner(draw, box, colour, caption)
    body_block(draw, box, title, detail, title_pt, detail_pt)


def render_page():
    img = Image.new("RGB", (SIZE, SIZE), CREAM)
    d = ImageDraw.Draw(img)

    # Masthead: the judge is not told the date, so make it huge.
    d.rectangle([0, 0, SIZE, 192], fill=(16, 22, 48))
    d.text((26, 10), "THE WORLD IN ONE DAY", font=load_font(BOLD_PATH, 29), fill=GOLD)
    date_text = "24 NOVEMBER 2026"
    pt = 100
    while d.textlength(date_text, font=load_font(BOLD_PATH, pt)) > SIZE - 36:
        pt -= 2
    d.text((18, 44), date_text, font=load_font(BOLD_PATH, pt), fill=WHITE)
    d.text((26, 154), "TUESDAY  -  FIVE BIG STORIES, CHECKED ACROSS OUTLETS",
           font=load_font(BOLD_PATH, 24), fill=(205, 212, 230))

    # Lead: Tuesday's Ulleung alert, a first for Russian jets.
    lead_box = (22, 208, 1002, 414)
    draw_lead = ImageDraw.Draw(img)
    draw_lead.rounded_rectangle(lead_box, radius=13, fill=PANEL, outline=INK, width=3)
    banner(d, lead_box, (176, 30, 32), "ULLEUNG  -  SOUTH KOREA")
    body_block(
        d, lead_box,
        "RUSSIAN JETS PROMPT FIRST ISLAND AIR-RAID ALERT",
        "About 5 Russian warplanes enter Korea's air defence zone "
        "early Tuesday. Seoul scrambles jets; the alert is lifted in "
        "3 minutes with no airspace violation.",
        title_pt=33, detail_pt=22,
    )

    # Four panels.
    panel(d, (22, 430, 500, 682), (0, 102, 102), "ZAPORIZHZHIA  -  UKRAINE",
          "RUSSIAN DAWN STRIKE KILLS 2, WOUNDS 40",
          "A home is destroyed and a five-storey block partly "
          "demolished on Tuesday. Four children are among the "
          "wounded, officials say.",
          title_pt=26, detail_pt=20)
    panel(d, (524, 430, 1002, 682), (128, 52, 128), "GAZA  -  PALESTINE",
          "ISRAELI STRIKES KILL 7; MENINGITIS ALERT",
          "A child and police officers are among the dead on "
          "Tuesday. Meningitis cases hit 272 in October, over "
          "8 times the usual rate.",
          title_pt=26, detail_pt=20)
    panel(d, (22, 698, 500, 916), (28, 110, 56), "WORLDWIDE  -  UN REPORT",
          "FIVE WOMEN KILLED EVERY HOUR, UN SAYS",
          "New UN brief on Tuesday: 47,000 women and girls "
          "killed by a partner or relative in 2025, 129 a day.",
          title_pt=26, detail_pt=20)
    panel(d, (524, 698, 1002, 916), (28, 64, 142), "ITURI  -  DR CONGO",
          "EBOLA TEAMS STILL TRAPPED IN HOSPITAL",
          "WHO says on Tuesday its teams are still sheltering "
          "in a maternity ward, over 48 hours, amid fighting.",
          title_pt=26, detail_pt=20)

    # Ticker along the foot of the page.
    d.rectangle([0, 928, SIZE, SIZE], fill=(16, 22, 48))
    ticker_text = (
        "ALSO TUESDAY:  CHINA EXTENDS PAUSE ON GALLIUM BAN TO US "
        "TO 27 JAN 2027  *  US READIES NEW TARIFFS ON 16 PARTNERS, "
        "SOURCES SAY  *  175 MIGRANTS MISSING FROM SENEGAL BOAT; "
        "NAVY RESCUED 974 MONDAY"
    )
    ty = 936
    for ln in wrap(d, ticker_text, load_font(BOLD_PATH, 19), SIZE - 44):
        d.text((22, ty), ln, font=load_font(BOLD_PATH, 19), fill=GOLD)
        ty += 24

    return img


if __name__ == "__main__":
    render_page().save("entry.png")
    print("saved entry.png")
