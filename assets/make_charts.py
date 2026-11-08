"""Generate the two README charts for the NYC yellow taxi repo.
All numbers are the verified figures from the TLC Annual Report 2024
and the published August 2024 analysis. No other numbers are used.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(OUT, exist_ok=True)

TEAL = "#0f766e"
GREY = "#94a3b8"
DARK = "#1f2937"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.edgecolor": "#d1d5db",
    "axes.labelcolor": DARK,
    "text.color": DARK,
    "xtick.color": DARK,
    "ytick.color": DARK,
})

# --- Chart 1: what a trip costs, by direction (August 2024 analysis) ---
labels = ["Within\nManhattan", "Into\nManhattan", "Out of\nManhattan"]
fares = [14.41, 26.62, 33.91]        # average fare, USD
distances = [2.16, 4.47, 3.57]       # average distance, miles
durations = [13.17, 21.09, 22.54]    # average duration, minutes

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
ax = axes[0]
bars = ax.bar(labels, fares, color=TEAL, width=0.6)
ax.set_title("Average fare ($)", fontsize=12, fontweight="bold")
ax.set_ylabel("Dollars")
ax.spines[["top", "right"]].set_visible(False)
for b, v in zip(bars, fares):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.8, f"${v:.2f}",
            ha="center", fontsize=11)
ax.set_ylim(0, 40)

ax = axes[1]
bars = ax.bar(labels, distances, color=TEAL, width=0.6)
ax.set_title("Average distance (miles)", fontsize=12, fontweight="bold")
ax.set_ylabel("Miles")
ax.spines[["top", "right"]].set_visible(False)
for b, v in zip(bars, distances):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.12, f"{v:.2f}",
            ha="center", fontsize=11)
ax.set_ylim(0, 5.2)

fig.suptitle("What a yellow-taxi trip costs — August 2024 (TLC trip data)",
             fontsize=13, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.92])
fig.savefig(os.path.join(OUT, "trip-cost-by-direction.png"), dpi=150)
plt.close(fig)

# --- Chart 2: 2024 vs 2021, full-year totals (TLC Annual Report) ---
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
ax = axes[0]
bars = ax.bar(["2021", "2024"], [31, 41.17], color=[GREY, TEAL], width=0.55)
ax.set_title("Yellow-taxi trips (millions)", fontsize=12, fontweight="bold")
ax.set_ylabel("Trips (millions)")
ax.spines[["top", "right"]].set_visible(False)
for b, v in zip(bars, [31, 41.17]):
    ax.text(b.get_x() + b.get_width() / 2, v + 1, f"{v:.2f}M" if v > 31 else "~31M",
            ha="center", fontsize=11)
ax.set_ylim(0, 48)

ax = axes[1]
bars = ax.bar(["2021", "2024"], [486, 966], color=[GREY, TEAL], width=0.55)
ax.set_title("Farebox revenue ($ millions)", fontsize=12, fontweight="bold")
ax.set_ylabel("$ millions")
ax.spines[["top", "right"]].set_visible(False)
for b, v in zip(bars, [486, 966]):
    label = "~$486M" if v == 486 else "$966M"
    ax.text(b.get_x() + b.get_width() / 2, v + 25, label,
            ha="center", fontsize=11)
ax.set_ylim(0, 1100)

fig.suptitle("Yellow taxis bounced back — 2021 vs 2024 (TLC Annual Report)",
             fontsize=13, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.92])
fig.savefig(os.path.join(OUT, "trips-and-farebox-2021-vs-2024.png"), dpi=150)
plt.close(fig)

print("charts written to", OUT)
