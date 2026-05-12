import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os

# ── Setup ──────────────────────────────────────────────────────────────────────
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH  = os.path.join(os.path.dirname(OUTPUT_DIR), "cleancardata.csv")

sns.set_theme(style="darkgrid")
plt.rcParams.update({"figure.dpi": 150, "font.family": "DejaVu Sans"})

data = pd.read_csv(DATA_PATH)

# ── 1. Price Category Distribution (Bar Chart) ─────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
order = data["price_category"].value_counts().index
palette = sns.color_palette("viridis", len(order))
sns.countplot(x="price_category", data=data, order=order, hue="price_category",
              palette=palette, legend=False, ax=ax)
ax.set_title("Car Price Category Distribution", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Price Category", fontsize=11)
ax.set_ylabel("Count", fontsize=11)
for bar in ax.patches:
    ax.annotate(f'{int(bar.get_height())}',
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                ha="center", va="bottom", fontsize=10, fontweight="bold")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "01_price_category_distribution.png"))
plt.close()
print("Chart 1 saved: Price Category Distribution")

# ── 2. Selling Price vs Price Category (Box Plot) ──────────────────────────────
cat_order = [c for c in ["Low", "Mid", "High"] if c in data["price_category"].unique()]
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="price_category", y="selling_price", data=data,
            palette="Set2", order=cat_order, hue="price_category",
            legend=False, ax=ax)
ax.set_title("Selling Price by Price Category", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Price Category", fontsize=11)
ax.set_ylabel("Selling Price (Rs.)", fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e5:.1f}L"))
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "02_selling_price_by_category.png"))
plt.close()
print("Chart 2 saved: Selling Price by Category")

# ── 3. Top 10 Car Brands by Count (Horizontal Bar) ────────────────────────────
fig, ax = plt.subplots(figsize=(8, 6))
top_brands = data["brand"].value_counts().head(10)
colors = sns.color_palette("mako", len(top_brands))
top_brands.sort_values().plot(kind="barh", ax=ax, color=colors[::-1])
ax.set_title("Top 10 Car Brands by Listing Count", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Count", fontsize=11)
ax.set_ylabel("Brand", fontsize=11)
for i, v in enumerate(top_brands.sort_values()):
    ax.text(v + 5, i, str(v), va="center", fontsize=9, fontweight="bold")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "03_top_brands.png"))
plt.close()
print("Chart 3 saved: Top 10 Brands")

# ── 4. Fuel Type Distribution (Pie Chart) ─────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 6))
fuel_counts = data["fuel"].value_counts()
colors = sns.color_palette("Set3", len(fuel_counts))
wedges, texts, autotexts = ax.pie(fuel_counts, labels=fuel_counts.index,
                                   autopct="%1.1f%%", colors=colors,
                                   startangle=140, pctdistance=0.82,
                                   wedgeprops=dict(width=0.6))
for text in autotexts:
    text.set_fontsize(10)
    text.set_fontweight("bold")
ax.set_title("Fuel Type Distribution", fontsize=14, fontweight="bold", pad=12)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "04_fuel_type_distribution.png"))
plt.close()
print("Chart 4 saved: Fuel Type Distribution")

# ── 5. Transmission Type Count (Bar Chart) ────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 5))
sns.countplot(x="transmission", data=data, hue="transmission",
              palette=["#4C72B0", "#DD8452", "#55A868"], legend=False, ax=ax)
ax.set_title("Transmission Type Distribution", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Transmission", fontsize=11)
ax.set_ylabel("Count", fontsize=11)
for bar in ax.patches:
    ax.annotate(f'{int(bar.get_height())}',
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                ha="center", va="bottom", fontsize=11, fontweight="bold")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "05_transmission_distribution.png"))
plt.close()
print("Chart 5 saved: Transmission Distribution")

# ── 6. Car Age vs Selling Price (Scatter Plot) ────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
scatter = ax.scatter(data["car_age"], data["selling_price"],
                     alpha=0.4, c=data["selling_price"],
                     cmap="plasma", s=20, edgecolors="none")
plt.colorbar(scatter, ax=ax, label="Selling Price (Rs.)")
ax.set_title("Car Age vs Selling Price", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Car Age (Years)", fontsize=11)
ax.set_ylabel("Selling Price (Rs.)", fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e5:.1f}L"))
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "06_car_age_vs_price.png"))
plt.close()
print("Chart 6 saved: Car Age vs Selling Price")

# ── 7. KM Driven Distribution (Histogram) ─────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(data["km_driven"].dropna(), bins=40, color="#2196F3", edgecolor="white", alpha=0.85)
ax.set_title("Distribution of KM Driven", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("KM Driven", fontsize=11)
ax.set_ylabel("Frequency", fontsize=11)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x/1000)}K"))
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "07_km_driven_distribution.png"))
plt.close()
print("Chart 7 saved: KM Driven Distribution")

# ── 8. Avg Selling Price by Brand (Top 8) ─────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
avg_price = (data.groupby("brand")["selling_price"]
               .mean()
               .sort_values(ascending=False)
               .head(8))
palette = sns.color_palette("rocket", len(avg_price))
avg_price.plot(kind="bar", ax=ax, color=palette, edgecolor="white")
ax.set_title("Average Selling Price - Top 8 Brands", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Brand", fontsize=11)
ax.set_ylabel("Avg Selling Price (Rs.)", fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e5:.1f}L"))
ax.tick_params(axis="x", rotation=30)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "08_avg_price_by_brand.png"))
plt.close()
print("Chart 8 saved: Avg Price by Brand")

print("\nAll 8 EDA charts saved to the eda_charts folder!")
