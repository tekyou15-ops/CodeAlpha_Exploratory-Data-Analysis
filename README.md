# CodeAlpha_Exploratory-Data-Analysis
A Codealpha -Data analytics Project task focusing on exploratory data analysis using the scraped data
# 📊 Biomedical Companies — Exploratory Data Analysis (EDA)


An exploratory data analysis (EDA) of the world's largest biomedical companies by revenue, uncovering trends, patterns, and insights from 2016 to 2025 using Python visualization libraries.

---

## 📋 Table of Contents
- [About](#about)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [EDA Tasks](#eda-tasks)
- [Key Findings](#key-findings)
- [Visualizations](#visualizations)
- [License](#license)

---

## 📌 About

This project performs a comprehensive **Exploratory Data Analysis (EDA)** on revenue data scraped from Wikipedia for the world's top biomedical companies. The analysis covers the period from **2016 to 2025**, examining revenue trends, country distributions, growth patterns, and revenue distributions. The goal is to identify meaningful patterns and insights that can support further research and decision-making in the biomedical industry.

**Data Source:** `biomedical_companies_cleaned.csv` (generated from the Web Scraping project)

---

## 🛠️ Technologies Used

| Library | Purpose |
|---|---|
| `Python 3.14` | Programming language |
| `pandas` | Data loading, cleaning, and manipulation |
| `matplotlib` | Base plotting and visualization |
| `seaborn` | Statistical data visualization |
| `re` | Data cleaning and text processing |

---

## 📁 Project Structure

```
biomedical-eda/
├── Task II-EDA.py                      # Main EDA script
├── biomedical_companies_cleaned.csv    # Input dataset
├── figures/
│   ├── revenue_trend.png               # Time trend plot
│   ├── revenue_distribution_2025.png   # Revenue distribution plot
│   ├── companies_by_country.png        # Country bar chart
│   └── top10_revenue_2025.png          # Top 10 companies bar chart
├── requirements.txt                    # Required libraries
└── README.md                           # Project documentation
```

---

## ⚙️ Installation

2. **Install required libraries**
```bash
pip install pandas matplotlib seaborn
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

> ⚠️ If using Python 3.14, use:
> ```bash
> "C:\Program Files\Python314\python.exe" -m pip install pandas matplotlib seaborn
> ```

---

## 🚀 Usage

1. **Make sure you have the CSV file** from the web scraping project:
```
biomedical_companies_cleaned.csv
```

2. **Run the EDA script:**
```Task II-EDA.py
---

## 🔍 EDA Tasks

### 1. ❓ Meaningful Questions Asked
- Which company has the highest revenue in 2025?
- Which countries dominate the biomedical industry?
- How has revenue changed from 2016 to 2025?
- Which companies grew the fastest?
- Are there any anomalies or outliers in the data?

### 2. 🔎 Data Structure Exploration
```python
print(df.shape)       # Rows and columns
print(df.dtypes)      # Data types
print(df.info())      # Full data info
print(df.describe())  # Statistical summary
```

### 3. 📈 Trends & Patterns
- Revenue growth trends from 2016 to 2025
- Country-wise company distribution
- Top 10 companies by 2025 revenue

### 4. 🧪 Hypotheses Tested
- **H1:** Johnson & Johnson consistently leads in revenue
- **H2:** COVID-19 caused a revenue spike for Pfizer in 2022
- **H3:** Eli Lilly shows the strongest recent growth

### 5. ⚠️ Data Issues Detected
- Missing revenue values (NaN) in some years
- Footnote references `[1]` embedded in revenue values
- Revenue stored as strings instead of numeric values

---

## 🔑 Key Findings

- **Johnson & Johnson** consistently ranked #1 from 2016 to 2025, growing from $72B to $94B
- **Pfizer** recorded a dramatic spike to ~$100B in 2022 due to COVID-19 vaccine revenues, before declining sharply
- **Eli Lilly & Co.** showed the strongest recent growth, accelerating rapidly from 2022 onward driven by diabetes and obesity drugs
- **Sinopharm** demonstrated remarkable growth, rising from modest revenues to approximately $84B by 2025
- **USA and China** dominate the top biomedical companies by number of entries
- The overall industry showed strong revenue growth over the decade, with most companies trending upward

---

## 📊 Visualizations

### 1. Revenue Trend of Top 10 Companies (2016–2025)
Line plot showing how revenue changed over time for each company.

### 2. Revenue Distribution (2025)
Histogram with KDE curve showing the spread of revenues across all companies in 2025, with mean and median reference lines.

### 3. Companies by Country
Bar chart showing how many top biomedical companies come from each country.

### 4. Top 10 Companies by Revenue (2025)
Horizontal bar chart ranking the top 10 companies by their 2025 revenue.

---

## 📈 Sample Visualizations Code

```python
# Time Trend Plot
sns.lineplot(data=df_melted, x="Year", y="Revenue", hue="Company", marker="o")

# Revenue Distribution
sns.histplot(df["2025"], bins=10, kde=True, color="#4C72B0")

# Companies by Country
df["Country"].value_counts().plot(kind="bar", color="steelblue")
```

---

## ⚠️ Limitations

- Data is sourced from Wikipedia and may contain inaccuracies
- Some revenue values were missing for certain years
- Revenue figures are in Billion USD and may use different accounting standards across companies
- Analysis covers only the top ranked companies — not the entire industry

---

## 📝 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 👤 Author

**Tekyo**
