# Task II- Exploratory Data Analysis
# Using scraped biomedical companies CSV data
#================================================
#================================================
#Preliminary Step: in CMD=install the required EDA Libraries
"C:\Program Files\Python314\python.exe" -m pip install pandas matplotlib seaborn
#================================================
#in Python IDLE
#================================================
# Step 1 - in python import the packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#================================================
# Step2- Load CSV data:
df = pd.read_csv("biomedical_companies.csv")
print(df.head())
#================================================
#Step 3 — Ask Meaningful Questions:
# 1. How many companies are in the datasets
print("Total companies:", len(df))
# 2. Which countries are represented?
print("Countries:", df["Country"].unique())
# 3. Which company has highest revenue?
print("Top company:", df.iloc[0])
# 4. How many companies per country?
print("\nCompanies per Country:")
print(df["Country"].value_counts())
#================================================
#Step 4 — Explore Data Structure:
# Shape of data
print("Rows & Columns:", df.shape)
# Column names
print("Columns:", df.columns.tolist())
# Data type — revenue should be numeric
print(df.dtypes)
print("\nData Types:\n", df.dtypes)
# Fix if revenue columns are strings
df["2025"] = pd.to_numeric(df["2025"], errors="coerce")
# First 5 rows
print(df.head())
# Last 5 rows
print(df.tail())
# Basic info
print(df.info())
#================================================
# Step 5 — Identify Trends, Patterns & Anomalies:
# Basic statistics
print(df.describe())
# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Check for duplicates
print("\nDuplicates:", df.duplicated().sum())
# Check for outliers
print("\nRevenue Stats:")
print(df["2025"].describe())
# Find anomalies — companies with no revenue data
print("\nCompanies with missing revenue:")
print(df[df["2025"].isnull()])
#================================================
#Step 6 — Test Hypotheses with Visualization:
# Plot 1 — Companies by Country (Bar Chart)
plt.figure(figsize=(10, 5))
df["Country"].value_counts().plot(kind="bar", color="steelblue")
plt.title("Number of Biomedical Companies by Country")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Plot 2 — Top 10 Companies by Revenue (2025)
plt.figure(figsize=(12, 6))
top10 = df.head(10)
sns.barplot(x="2025", y="Company", data=top10, palette="viridis")
plt.title("Top 10 Biomedical Companies by Revenue 2025")
plt.xlabel("Revenue (Billion USD)")
plt.tight_layout()
plt.show()
# Plot 3 — Revenue Distribution
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("biomedical_companies_cleaned.csv")
df["2025"] = pd.to_numeric(df["2025"], errors="coerce")
df = df.dropna(subset=["2025"])

# Set style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# Plot histogram
sns.histplot(
    df["2025"],
    bins=10,              # Fewer bins = cleaner look
    kde=True,
    color="#4C72B0",      # Nice blue color
    edgecolor="white",
    linewidth=0.8,
    alpha=0.85
)

# Add mean and median lines
mean_val = df["2025"].mean()
median_val = df["2025"].median()

plt.axvline(mean_val, color="red", linestyle="--", linewidth=1.5, label=f"Mean: ${mean_val:.1f}B")
plt.axvline(median_val, color="orange", linestyle="--", linewidth=1.5, label=f"Median: ${median_val:.1f}B")

# Labels and title
plt.title("Revenue Distribution of Biomedical Companies (2025)", fontsize=15, fontweight="bold", pad=15)
plt.xlabel("Revenue (Billion USD)", fontsize=12)
plt.ylabel("Number of Companies", fontsize=12)
plt.xticks(fontsize=10, rotation=0)
plt.yticks(fontsize=10)

# Legend
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("revenue_distribution_2025.png", dpi=300, bbox_inches="tight")
plt.show()

#================================================
# Step 7- Time Trend Plot====Key Steps
#================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned CSV
df = pd.read_csv("biomedical_companies_cleaned.csv")

# Year columns
year_columns = ['2025', '2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016']

# Convert to numeric
for col in year_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Select top 10
top10 = df.head(10)

# Melt to long format
df_melted = top10.melt(
    id_vars=["Company"],
    value_vars=year_columns,
    var_name="Year",
    value_name="Revenue"
)

df_melted["Year"] = pd.to_numeric(df_melted["Year"])
df_melted["Revenue"] = pd.to_numeric(df_melted["Revenue"], errors="coerce")

# Plot
plt.figure(figsize=(14, 7))
sns.lineplot(
    data=df_melted,
    x="Year",
    y="Revenue",
    hue="Company",
    marker="o"
)

plt.title("Revenue Trend of Top 10 Biomedical Companies", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Revenue (Billion USD)", fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=8)
plt.tight_layout()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
#================================================
#Complete EDA Summary:
print("=" * 50)
print("EDA SUMMARY REPORT")
print("=" * 50)
print(f"Total Companies: {len(df)}")
print(f"Total Columns: {len(df.columns)}")
print(f"Missing Values: {df.isnull().sum().sum()}")
print(f"Duplicate Rows: {df.duplicated().sum()}")
print(f"Countries Represented: {df['Country'].nunique()}")
print(f"Top Company: {df.iloc[0]['Company']}")
print("=" * 50)
