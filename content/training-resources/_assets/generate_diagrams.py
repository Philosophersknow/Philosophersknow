#!/usr/bin/env python3
"""
AIIPD Training Resources — Diagram Generator
============================================

Generates original technical diagrams for the training resource library.

WHY THIS EXISTS
---------------
Every image in a co-branded, commercially licensed product must be originally
created or fully assigned. Standard stock licences prohibit sub-licensing and
redistribution, which is exactly what the co-branding model does.
See content/governance/disclaimer-and-copyright-suite.md Section 6.

Diagrams produced by this script are original works, generated from code,
owned outright. No licensing exposure.

USAGE
-----
    python3 generate_diagrams.py            # generate all
    python3 generate_diagrams.py --list     # list available diagrams

OUTPUT
------
    diagrams/<slug>.png   at 300 DPI (print) — also usable on screen

© Liam Michael Clancy / Philosophersknow 2026
"""

import sys
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon, Circle, FancyArrowPatch

# ---------------------------------------------------------------------------
# House style
# ---------------------------------------------------------------------------

INK      = "#1A1A1A"
MUTED    = "#6B6B6B"
RULE     = "#D4D4D4"
PAPER    = "#FFFFFF"

# Semantic palette — chosen to remain distinguishable in greyscale print
# and to be legible for common colour vision deficiencies.
DANGER   = "#B3261E"   # stop / fatal / prohibited
WARN     = "#B26A00"   # caution / elevated risk
SAFE     = "#1F6F43"   # safe / permitted
INFO     = "#1F4E5F"   # neutral technical
ACCENT   = "#8C6D1F"   # highlight

DPI      = 300
FONT     = "Liberation Sans"

plt.rcParams.update({
    "font.family": FONT,
    "text.color": INK,
    "axes.edgecolor": RULE,
    "savefig.facecolor": PAPER,
    "figure.facecolor": PAPER,
})

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams")


def _finish(fig, ax, slug, title, subtitle=None):
    """Apply house furniture and save.

    Content must sit within y = 6..86. Anything placed outside the axes limits
    still appears in the saved image because bbox_inches="tight" expands to fit
    all artists — which silently collides with the footer. Do not place content
    at negative y.
    """
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    ax.text(0, 97, title, fontsize=15, fontweight="bold", va="top", ha="left")
    if subtitle:
        ax.text(0, 92.5, subtitle, fontsize=9.5, color=MUTED, va="top", ha="left")

    ax.plot([0, 100], [2.5, 2.5], color=RULE, lw=0.8)
    ax.text(0, 0.2, "© Liam Michael Clancy / Philosophersknow 2026 · AIIPD",
            fontsize=6.5, color=MUTED, va="bottom", ha="left")
    ax.text(100, 0.2, "Educational resource — not professional advice",
            fontsize=6.5, color=MUTED, va="bottom", ha="right")

    os.makedirs(OUTDIR, exist_ok=True)
    path = os.path.join(OUTDIR, f"{slug}.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print(f"  ✓ {slug}.png")
    return path


# ---------------------------------------------------------------------------
# 1. Hierarchy of Controls
#    Used by: CPCCWHS2001, RIIWHS201E, RIIRIS301E, BSBWHS311, HLTWHS002,
#             SITXWHS005, AURAFA004, CPCCCM2012
# ---------------------------------------------------------------------------

def hierarchy_of_controls():
    fig, ax = plt.subplots(figsize=(8.5, 6.4))

    levels = [
        ("ELIMINATE",    "Remove the hazard entirely",              SAFE,   "Most effective"),
        ("SUBSTITUTE",   "Replace with something less hazardous",   SAFE,   ""),
        ("ISOLATE",      "Separate people from the hazard",         INFO,   ""),
        ("ENGINEERING",  "Physical controls and modifications",     INFO,   ""),
        ("ADMINISTRATIVE","Procedures, training, signage",          WARN,   ""),
        ("PPE",          "Worn by the worker — last resort",        DANGER, "Least effective"),
    ]

    top_w, bot_w, cx = 34.0, 82.0, 50.0
    y0, h, gap = 12.0, 11.5, 1.4

    for i, (name, desc, col, note) in enumerate(levels):
        yb = y0 + (len(levels) - 1 - i) * (h + gap)
        f_b = i / (len(levels) - 1)
        f_t = (i + 1) / (len(levels) - 1)
        wb = top_w + (bot_w - top_w) * f_b
        wt = top_w + (bot_w - top_w) * f_t

        ax.add_patch(Polygon(
            [(cx - wt / 2, yb + h), (cx + wt / 2, yb + h),
             (cx + wb / 2, yb), (cx - wb / 2, yb)],
            closed=True, facecolor=col, edgecolor="white", lw=1.6, alpha=0.92))

        ax.text(cx, yb + h / 2 + 1.7, name, fontsize=10.5, fontweight="bold",
                color="white", ha="center", va="center")
        ax.text(cx, yb + h / 2 - 2.4, desc, fontsize=7.8,
                color="white", ha="center", va="center")
        if note:
            # bottom band is widest — place its note above the band to avoid collision
            ny = yb + h + 3.0 if i == len(levels) - 1 else yb + h / 2
            ax.text(97, ny, note, fontsize=8, fontweight="bold",
                    color=col, ha="right", va="center")

    ax.annotate("", xy=(5, y0 + 0.5), xytext=(5, y0 + 6 * (h + gap)),
                arrowprops=dict(arrowstyle="-|>", lw=1.8, color=MUTED))
    ax.text(3.2, y0 + 3 * (h + gap), "DECREASING EFFECTIVENESS", fontsize=7.6,
            color=MUTED, rotation=90, ha="center", va="center", fontweight="bold")

    ax.text(cx, 7.0,
            "Levels 1–4 protect regardless of what the worker does.\n"
            "Levels 5–6 depend on human behaviour — which is why they come last.",
            fontsize=8.4, ha="center", va="center", color=INK, style="italic")

    return _finish(fig, ax, "hierarchy-of-controls", "The Hierarchy of Controls",
                   "Apply controls in order. A lower level is only acceptable where the higher levels are not reasonably practicable.")


# ---------------------------------------------------------------------------
# 2. Temperature Danger Zone
#    Used by: SITXFSA005, SITXFSA006, SITHCCC029, SITXINV006, SITHCCC042
# ---------------------------------------------------------------------------

def temperature_danger_zone():
    fig, ax = plt.subplots(figsize=(8.5, 6.6))

    bx, bw = 22, 20
    y_lo, y_hi = 10, 84

    def to_y(t):
        return y_lo + (t + 20) / (100 + 20) * (y_hi - y_lo)

    ax.add_patch(Rectangle((bx, to_y(-20)), bw, to_y(5) - to_y(-20),
                           facecolor=INFO, alpha=0.85, edgecolor="white", lw=1.2))
    ax.add_patch(Rectangle((bx, to_y(5)), bw, to_y(60) - to_y(5),
                           facecolor=DANGER, alpha=0.90, edgecolor="white", lw=1.2))
    ax.add_patch(Rectangle((bx, to_y(60)), bw, to_y(100) - to_y(60),
                           facecolor=SAFE, alpha=0.85, edgecolor="white", lw=1.2))

    ax.text(bx + bw / 2, (to_y(-20) + to_y(5)) / 2, "COLD\nSafe", fontsize=9.5,
            fontweight="bold", color="white", ha="center", va="center")
    ax.text(bx + bw / 2, (to_y(5) + to_y(60)) / 2,
            "TEMPERATURE\nDANGER ZONE\n\n5 °C – 60 °C\n\nBacteria multiply\nrapidly",
            fontsize=10, fontweight="bold", color="white", ha="center", va="center")
    ax.text(bx + bw / 2, (to_y(60) + to_y(100)) / 2, "HOT\nSafe", fontsize=9.5,
            fontweight="bold", color="white", ha="center", va="center")

    for t, lab in [(-18, "−18 °C  Frozen storage"), (5, "5 °C  Cold storage max"),
                   (60, "60 °C  Hot holding min"), (75, "75 °C  Cooking core temp")]:
        ax.plot([bx - 2.5, bx], [to_y(t), to_y(t)], color=INK, lw=1.1)
        ax.text(bx - 3.5, to_y(t), lab, fontsize=8.4, ha="right", va="center")

    px = 50
    ax.text(px, 84, "THE 2-HOUR / 4-HOUR RULE", fontsize=10, fontweight="bold", va="top")
    ax.text(px, 79.5, "Cumulative time in the danger zone", fontsize=8, color=MUTED, va="top")

    rules = [
        ("Under 2 hours", "Use, or refrigerate for later use", SAFE),
        ("2 – 4 hours",   "Use immediately.\nMust not return to refrigeration", WARN),
        ("Over 4 hours",  "DISCARD", DANGER),
    ]
    ry = 71
    for band, action, col in rules:
        ax.add_patch(FancyBboxPatch((px, ry - 9), 46, 8.6,
                                    boxstyle="round,pad=0.25,rounding_size=0.6",
                                    facecolor=col, alpha=0.13, edgecolor=col, lw=1.3))
        ax.text(px + 1.6, ry - 2.2, band, fontsize=8.8, fontweight="bold", color=col, va="top")
        ax.text(px + 1.6, ry - 5.2, action, fontsize=7.8, va="top", color=INK)
        ry -= 11.5

    ax.text(px, 33, "COOLING — TWO STAGES", fontsize=10, fontweight="bold", va="top")
    ax.add_patch(FancyBboxPatch((px, 16.5), 46, 13.5,
                                boxstyle="round,pad=0.3,rounding_size=0.6",
                                facecolor=ACCENT, alpha=0.10, edgecolor=ACCENT, lw=1.3))
    ax.text(px + 1.8, 28.0, "60 °C  →  21 °C     within 2 hours", fontsize=9,
            fontweight="bold", va="top")
    ax.text(px + 1.8, 24.2, "21 °C  →  5 °C       within a further 4 hours", fontsize=9,
            fontweight="bold", va="top")
    ax.text(px + 1.8, 20.0,
            "A large stockpot on the bench will not achieve this.\n"
            "Divide into shallow containers.", fontsize=7.6, va="top", color=MUTED)

    ax.text(px, 12,
            "Reheating does not undo it — heat-stable toxins\nsurvive cooking temperatures.",
            fontsize=8.2, va="top", color=DANGER, fontweight="bold")

    return _finish(fig, ax, "temperature-danger-zone", "The Temperature Danger Zone",
                   "Food safety — time and temperature control")


# ---------------------------------------------------------------------------
# 3. Fall Clearance Calculation
#    Used by: CPCCCM2012
# ---------------------------------------------------------------------------

def fall_clearance():
    fig, ax = plt.subplots(figsize=(8.5, 6.6))

    ax.plot([12, 12], [18, 82], color=INK, lw=2.2)
    ax.text(12, 84, "Anchor point", fontsize=8.6, ha="center", fontweight="bold")
    ax.add_patch(Circle((12, 82), 1.3, facecolor=INK))
    ax.plot([6, 50], [18, 18], color=INK, lw=2.4)
    ax.text(51.5, 18, "Surface below", fontsize=8.2, ha="left", va="center", color=MUTED)

    segs = [
        (82, 68, "Lanyard length",           "2.00 m", INFO),
        (68, 55, "Shock absorber deployment", "1.75 m", WARN),
        (55, 44, "Worker height below D-ring", "1.50 m", INFO),
        (44, 32, "Safety margin",             "1.00 m", DANGER),
    ]

    for ytop, ybot, label, val, col in segs:
        ax.add_patch(Rectangle((9.4, ybot), 5.2, ytop - ybot,
                               facecolor=col, alpha=0.30, edgecolor=col, lw=1.2))
        ax.annotate("", xy=(19, ybot), xytext=(19, ytop),
                    arrowprops=dict(arrowstyle="<|-|>", lw=1.2, color=col))
        ax.text(21.5, (ytop + ybot) / 2 + 1.2, label, fontsize=8.4, va="center", fontweight="bold")
        ax.text(21.5, (ytop + ybot) / 2 - 2.2, val, fontsize=8.4, va="center", color=col,
                fontweight="bold")

    ax.plot([6, 17], [32, 32], color=DANGER, lw=1.4, ls="--")
    ax.text(6, 29.0, "Lowest point reached", fontsize=7.8, color=DANGER, fontweight="bold")

    ax.add_patch(FancyBboxPatch((56, 52), 42, 26,
                                boxstyle="round,pad=0.4,rounding_size=0.8",
                                facecolor=DANGER, alpha=0.10, edgecolor=DANGER, lw=1.6))
    ax.text(58, 74.5, "TOTAL CLEARANCE REQUIRED", fontsize=9.6, fontweight="bold",
            color=DANGER, va="top")
    ax.text(58, 69.5, "2.00  +  1.75  +  1.50  +  1.00", fontsize=10, va="top")
    ax.plot([58, 92], [66.5, 66.5], color=DANGER, lw=1.1)
    ax.text(58, 64.5, "≈ 6.25 metres", fontsize=15, fontweight="bold", color=DANGER, va="top")
    ax.text(58, 57.5,
            "below the anchor point, before the\nsystem can arrest the fall.",
            fontsize=8.2, va="top", color=INK)

    ax.add_patch(FancyBboxPatch((56, 20), 42, 27,
                                boxstyle="round,pad=0.4,rounding_size=0.8",
                                facecolor=WARN, alpha=0.10, edgecolor=WARN, lw=1.4))
    ax.text(58, 44, "WHY THIS MATTERS", fontsize=9.2, fontweight="bold", color=WARN, va="top")
    ax.text(58, 39.5,
            "On a two-storey residential frame there\n"
            "is frequently NOT 6.25 m of clear space.\n\n"
            "A fall arrest system without adequate\n"
            "clearance does not arrest the fall.\n"
            "You strike the ground wearing a harness.",
            fontsize=8.0, va="top", color=INK)

    ax.text(50, 11.0,
            "Use the manufacturer's stated free-fall and deployment figures for the actual equipment.\n"
            "An inertia reel arrests over a much shorter distance and may be the only viable option.",
            fontsize=7.6, ha="center", va="top", color=MUTED, style="italic")

    return _finish(fig, ax, "fall-arrest-clearance", "Fall Arrest — Clearance Calculation",
                   "Why a standard shock-absorbing lanyard may be unusable at low heights")


# ---------------------------------------------------------------------------
# 4. Refrigerator Storage Hierarchy
#    Used by: SITXFSA006, SITXINV006, SITHCCC042
# ---------------------------------------------------------------------------

def fridge_storage_order():
    fig, ax = plt.subplots(figsize=(8.5, 6.4))

    ax.add_patch(FancyBboxPatch((14, 10), 52, 76,
                                boxstyle="round,pad=0.5,rounding_size=1.2",
                                facecolor="#F4F7F8", edgecolor=INK, lw=2.0))

    shelves = [
        ("Ready-to-eat · cooked food · dairy", "No further cooking step", SAFE),
        ("Raw whole cuts — beef, pork, lamb",  "Lower cook temp required", INFO),
        ("Raw mince · raw seafood",            "Higher risk — cut surfaces", WARN),
        ("RAW POULTRY",                        "Highest cook temp — 75 °C core", DANGER),
    ]

    sy, sh = 70, 15.5
    for i, (label, note, col) in enumerate(shelves):
        y = sy - i * sh
        ax.add_patch(Rectangle((17, y), 46, 12.4, facecolor=col, alpha=0.16,
                               edgecolor=col, lw=1.3))
        ax.plot([17, 63], [y, y], color=INK, lw=1.6)
        ax.text(19, y + 8.0, label, fontsize=8.8, fontweight="bold", va="center")
        ax.text(19, y + 4.0, note, fontsize=7.4, color=MUTED, va="center")

    ax.annotate("", xy=(70, 14), xytext=(70, 80),
                arrowprops=dict(arrowstyle="-|>", lw=2.0, color=DANGER))
    ax.text(72.5, 47, "INCREASING REQUIRED\nCOOKING TEMPERATURE",
            fontsize=8.0, color=DANGER, fontweight="bold", va="center", ha="left")

    ax.add_patch(FancyBboxPatch((72, 60), 27, 22,
                                boxstyle="round,pad=0.35,rounding_size=0.7",
                                facecolor=ACCENT, alpha=0.10, edgecolor=ACCENT, lw=1.3))
    ax.text(73.5, 79, "THE PRINCIPLE", fontsize=8.6, fontweight="bold", va="top")
    ax.text(73.5, 75,
            "Anything that drips\nfalls onto food that\nrequires a HIGHER\ncooking temperature —\n"
            "never onto ready-\nto-eat food.",
            fontsize=7.6, va="top")

    ax.text(40, 5.5,
            "Cover everything · store off the floor · do not overload — air must circulate\n"
            "Never store food in an opened can",
            fontsize=7.8, ha="center", va="center", color=MUTED, style="italic")

    return _finish(fig, ax, "fridge-storage-order", "Refrigerator Storage Hierarchy",
                   "Store from top to bottom in order of required cooking temperature")


# ---------------------------------------------------------------------------
# 5. Roof Geometry — Common and Hip Rafter
#    Used by: CPCCCA3002
# ---------------------------------------------------------------------------

def roof_geometry():
    """Content within y = 6..86."""
    fig, ax = plt.subplots(figsize=(8.8, 6.2))

    ox, oy = 8, 34
    run, rise = 40.0, 20.0

    # triangle
    ax.plot([ox, ox + run], [oy, oy], color=INK, lw=2.2)                    # run
    ax.plot([ox + run, ox + run], [oy, oy + rise], color=INK, lw=1.5, ls="--")  # rise
    ax.plot([ox, ox + run], [oy, oy + rise], color=INFO, lw=3.2)           # true length

    ax.text(ox + run / 2 + 6, oy - 3.0, "RUN  (half span − ½ ridge)", fontsize=8.2,
            ha="center", va="top", fontweight="bold")
    ax.text(ox + run - 1.8, oy + rise / 2, "RISE", fontsize=8.2, va="center",
            ha="right", fontweight="bold")
    ax.text(ox + run / 2 - 3, oy + rise / 2 + 3.4, "TRUE LENGTH", fontsize=8.2,
            color=INFO, fontweight="bold", rotation=26.6, ha="center")

    # pitch angle marker
    ax.plot([ox + 5.5, ox + 5.5], [oy, oy + 2.75], color=MUTED, lw=0.9)
    ax.text(ox + 6.8, oy + 1.3, "pitch", fontsize=7.4, color=MUTED, va="center")

    # plan-view inset: common run vs hip run at 45°
    px0, py0 = 14, 11
    sq = 14
    ax.add_patch(Rectangle((px0, py0), sq, sq, facecolor="none",
                           edgecolor=MUTED, lw=1.0, ls=":"))
    ax.plot([px0, px0 + sq], [py0, py0], color=INFO, lw=2.4)
    ax.plot([px0, px0 + sq], [py0, py0 + sq], color=ACCENT, lw=2.4, ls=(0, (5, 2)))
    ax.text(px0 + sq / 2, py0 - 2.2, "common run", fontsize=7.0, color=INFO,
            ha="center", va="top", fontweight="bold")
    ax.text(px0 + sq + 1.5, py0 + sq - 1.0, "hip run × 1.414", fontsize=7.0,
            color=ACCENT, ha="left", va="center", fontweight="bold")
    ax.text(px0 - 1.5, py0 + sq / 2, "PLAN\nVIEW", fontsize=7.2, color=MUTED,
            ha="right", va="center", fontweight="bold")

    # common rafter box
    ax.add_patch(FancyBboxPatch((56, 52), 42, 30,
                                boxstyle="round,pad=0.4,rounding_size=0.8",
                                facecolor=INFO, alpha=0.08, edgecolor=INFO, lw=1.3))
    ax.text(57.6, 79.5, "COMMON RAFTER", fontsize=9.4, fontweight="bold",
            color=INFO, va="top")
    ax.text(57.6, 74.5,
            "Rise     = Run × tan(pitch)\n\n"
            "True len = √(Run² + Rise²)\n"
            "         = Run ÷ cos(pitch)\n\n"
            "Multiplier = 1 ÷ cos(pitch)",
            fontsize=8.0, va="top", family="monospace")

    # hip rafter box
    ax.add_patch(FancyBboxPatch((56, 16), 42, 32,
                                boxstyle="round,pad=0.4,rounding_size=0.8",
                                facecolor=ACCENT, alpha=0.10, edgecolor=ACCENT, lw=1.3))
    ax.text(57.6, 45.5, "HIP RAFTER", fontsize=9.4, fontweight="bold",
            color=ACCENT, va="top")
    ax.text(57.6, 40.5,
            "Hip run = Common run × 1.414\n"
            "          (45° in plan → √2)\n\n"
            "Same RISE over a LONGER run\n"
            "→ shallower pitch than commons\n"
            "→ hip needs its OWN bevels",
            fontsize=8.0, va="top", family="monospace")

    ax.text(56, 10.0,
            "The most common roof-cutting error is\nusing the common rafter bevel on a hip.",
            fontsize=8.2, ha="left", va="center", color=DANGER,
            fontweight="bold", style="italic")

    return _finish(fig, ax, "roof-geometry-common-hip",
                   "Roof Geometry — Common and Hip Rafters",
                   "Why a hip rafter requires its own plumb and level bevels")


# ---------------------------------------------------------------------------
# 6. Trench Safety — Cross Section
#    Used by: RIIWHS201E, RIICWD201D, RIIRIS301E
# ---------------------------------------------------------------------------

def trench_cross_section():
    """All content must sit within y = 6..86. Below y=5 is reserved for the footer."""
    fig, ax = plt.subplots(figsize=(8.8, 6.6))

    # --- ground mass and surface -------------------------------------------
    gy0, gy1 = 40, 78          # ground body
    ax.add_patch(Rectangle((5, gy0), 90, gy1 - gy0,
                           facecolor="#E8DFD3", edgecolor=MUTED, lw=1.0))
    ax.plot([5, 95], [gy1, gy1], color=INK, lw=2.2)

    # --- trench void and shield --------------------------------------------
    tx0, tx1 = 42, 60
    ty0 = 44
    ax.add_patch(Rectangle((tx0, ty0), tx1 - tx0, gy1 - ty0,
                           facecolor=PAPER, edgecolor=INK, lw=1.5))
    ax.add_patch(Rectangle((tx0 + 0.8, ty0 + 0.6), tx1 - tx0 - 1.6, gy1 - ty0 - 0.6,
                           facecolor="none", edgecolor=INFO, lw=3.2))
    ax.text((tx0 + tx1) / 2, (ty0 + gy1) / 2 - 2, "TRENCH\nSHIELD", fontsize=8.6,
            fontweight="bold", color=INFO, ha="center", va="center")

    # --- depth dimension ----------------------------------------------------
    ax.annotate("", xy=(39, ty0), xytext=(39, gy1),
                arrowprops=dict(arrowstyle="<|-|>", lw=1.3, color=INK))
    ax.text(37.4, (ty0 + gy1) / 2, "DEPTH", fontsize=8.2, rotation=90,
            ha="right", va="center", fontweight="bold")

    # --- ladder -------------------------------------------------------------
    lx = tx0 + 2.6
    ax.plot([lx, lx], [ty0 + 1, gy1 + 1.5], color=WARN, lw=2.0)
    for yy in range(int(ty0) + 3, int(gy1), 4):
        ax.plot([lx - 1.0, lx + 1.0], [yy, yy], color=WARN, lw=1.3)
    ax.annotate("Ladder within reach", xy=(lx, ty0 + 6), xytext=(20, 46),
                fontsize=7.6, color=WARN, fontweight="bold", va="center",
                arrowprops=dict(arrowstyle="-", lw=0.9, color=WARN))

    # --- spoil, set back ----------------------------------------------------
    ax.add_patch(Polygon([(70, gy1), (86, gy1), (81, gy1 + 7), (75, gy1 + 7)],
                         closed=True, facecolor="#C8B49A", edgecolor=MUTED, lw=1.0))
    ax.text(78, gy1 + 8.6, "SPOIL", fontsize=8.0, ha="center", fontweight="bold")
    ax.annotate("", xy=(tx1, gy1 + 3.2), xytext=(70, gy1 + 3.2),
                arrowprops=dict(arrowstyle="<|-|>", lw=1.2, color=DANGER))
    ax.text(65, gy1 + 4.8, "min 1 m", fontsize=7.6, ha="center",
            color=DANGER, fontweight="bold")

    # --- plant set back -----------------------------------------------------
    ax.plot([20, 32], [gy1, gy1], color=DANGER, lw=4.0, solid_capstyle="butt")
    ax.text(26, gy1 + 2.4, "PLANT SET BACK", fontsize=7.6, ha="center",
            color=DANGER, fontweight="bold")

    # --- legend (left) ------------------------------------------------------
    items = [
        ("Spoil min 1 m from edge",  "Spoil at the edge surcharges the wall", DANGER),
        ("Plant set back",           "Weight and vibration destabilise the face", DANGER),
        ("Support to suit ground",   "Batter, shore or shield — competent person decides", INFO),
        ("Access within reach",      "Ladder close to any person in the trench", WARN),
        ("Reinspect after rain",     "Water changes wall stability", WARN),
    ]
    by = 33.5
    for label, note, col in items:
        ax.plot(6.2, by, marker="s", markersize=5.5, color=col)
        ax.text(9.0, by + 1.1, label, fontsize=7.8, fontweight="bold", va="center")
        ax.text(9.0, by - 1.9, note, fontsize=6.9, color=MUTED, va="center")
        by -= 6.0

    # --- why it matters (right) --------------------------------------------
    ax.add_patch(FancyBboxPatch((60, 8.5), 38, 24,
                                boxstyle="round,pad=0.35,rounding_size=0.7",
                                facecolor=DANGER, alpha=0.10, edgecolor=DANGER, lw=1.4))
    ax.text(61.6, 29.5, "WHY IT MATTERS", fontsize=8.8, fontweight="bold",
            color=DANGER, va="top")
    ax.text(61.6, 25.5,
            "1 m³ of soil ≈ 1.5–2 tonnes.\n"
            "Burial to chest height causes\n"
            "fatal crush asphyxiation.\n"
            "Workers do not self-rescue.",
            fontsize=7.6, va="top")

    return _finish(fig, ax, "trench-safety-cross-section",
                   "Excavation Safety — Cross Section",
                   "Support, spoil setback, plant setback and access")


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

DIAGRAMS = {
    "hierarchy-of-controls":       (hierarchy_of_controls,
        "CPCCWHS2001, RIIWHS201E, RIIRIS301E, BSBWHS311, HLTWHS002, SITXWHS005, AURAFA004"),
    "temperature-danger-zone":     (temperature_danger_zone,
        "SITXFSA005, SITXFSA006, SITHCCC029, SITXINV006, SITHCCC042"),
    "fall-arrest-clearance":       (fall_clearance,
        "CPCCCM2012, CPCCCA3004"),
    "fridge-storage-order":        (fridge_storage_order,
        "SITXFSA006, SITXINV006, SITHCCC042"),
    "roof-geometry-common-hip":    (roof_geometry,
        "CPCCCA3002"),
    "trench-safety-cross-section": (trench_cross_section,
        "RIIWHS201E, RIICWD201D, RIIRIS301E"),
}


def main():
    if "--list" in sys.argv:
        print("\nAvailable diagrams:\n")
        for slug, (_, used_by) in DIAGRAMS.items():
            print(f"  {slug}")
            print(f"      used by: {used_by}\n")
        return

    print(f"\nGenerating {len(DIAGRAMS)} diagrams → {OUTDIR}\n")
    for slug, (fn, _) in DIAGRAMS.items():
        fn()
    print(f"\nDone. {len(DIAGRAMS)} diagrams generated.\n")
    print("All diagrams are original works generated from code — owned outright,")
    print("no third-party licensing exposure. Safe for co-branded distribution.\n")


if __name__ == "__main__":
    main()
