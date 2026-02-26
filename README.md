# 🏥 Do Richer Neighborhoods Live Longer?
### Analyzing the Link Between Income and Health Outcomes Across U.S. Counties

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![SQL](https://img.shields.io/badge/SQL-SQLite-orange?logo=sqlite)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)
![Tableau](https://img.shields.io/badge/Tableau-Public-lightblue?logo=tableau)

> *"In America, your zip code predicts your lifespan. Counties with higher income live up to 10+ years longer than poorer ones — here's the data."*

---

## 📌 Project Overview

This end-to-end data analytics project explores the relationship between household income and health outcomes (life expectancy, mortality rates) across U.S. counties — using real CDC and Census Bureau data.

**Key Questions:**
- Do higher-income counties have longer life expectancies?
- Which states have the worst income-health gap?
- How has this relationship changed over time?

---

## 🛠️ Tech Stack

| Tool | Role |
|------|------|
| 🐍 Python | Data collection, cleaning, loading to SQL |
| 🗄️ SQL (SQLite) | Data storage & business queries |
| 📊 Power BI | Executive KPI dashboard |
| 📈 Tableau | Public storytelling visualization |

---

## 📁 Project Structure

```
health-outcomes-analysis/
│
├── data/                        # Raw downloaded CSVs (not committed to git)
│   └── README.md                # Instructions to download data
│
├── src/
│   ├── data_loader.py           # Download & clean CDC + Census data
│   └── db_loader.py             # Load cleaned data into SQLite
│
├── sql/
│   ├── schema.sql               # Create database tables
│   └── queries.sql              # Key business analysis queries
│
├── notebooks/
│   └── 01_EDA.ipynb             # Exploratory Data Analysis
│
├── health_outcomes.db           # SQLite database (auto-generated)
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Mlamichhane1/health-outcomes-analysis.git
cd health-outcomes-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the data
Follow instructions in `data/README.md`

### 4. Run the pipeline
```bash
# Step 1: Clean data & build SQLite database
python src/data_loader.py
python src/db_loader.py
```

### 5. Open dashboards
- **Power BI:** Open `health_outcomes.pbix`, connect to `health_outcomes.db`
- **Tableau:** Open Tableau Desktop, connect to `health_outcomes.db`

---

## 📊 Dashboard Previews

### Power BI — Executive KPI Dashboard
> *Screenshot coming soon*

### Tableau — Storytelling Visualization
> 🔗 Tableau Public link coming soon

---

## 💡 Key Insights

- Counties in the **top income quartile** live on average **X years longer** than the bottom quartile
- **State X** has the largest income-health gap
- The relationship between income and life expectancy has **grown stronger since XXXX**

*(Update these after analysis!)*

---

## 📚 References

- [CDC WONDER Database](https://wonder.cdc.gov/)
- [U.S. Census Bureau — Income Data](https://www.census.gov/topics/income-poverty/income.html)
- Chetty, R. et al. (2016). *The Association Between Income and Life Expectancy in the United States*. JAMA.
- Course: Using Big Data to Solve Economic and Social Problems

---

## 👤 Author

**Madhav Lamichhane**
[LinkedIn](https://www.linkedin.com/in/madhav-lamichhane-33304b264/) | [GitHub](https://github.com/Mlamichhane1)
