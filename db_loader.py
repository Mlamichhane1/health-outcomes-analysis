"""
db_loader.py
------------
Step 2 of the pipeline: Load cleaned CSV into SQLite database.
Output: health_outcomes.db (SQLite)
"""

import sqlite3
import pandas as pd
import os

CLEANED_DATA_PATH = "data/cleaned_health_income.csv"
DB_PATH = "health_outcomes.db"
SCHEMA_PATH = "sql/schema.sql"


def create_database(conn: sqlite3.Connection):
    """Create tables using schema.sql."""
    print("🗄️  Creating database schema...")
    with open(SCHEMA_PATH, "r") as f:
        schema = f.read()
    conn.executescript(schema)
    conn.commit()
    print("   ✅ Schema created")


def load_data_to_db(conn: sqlite3.Connection, df: pd.DataFrame):
    """Load cleaned DataFrame into SQLite."""
    print("📤 Loading data into SQLite...")
    df.to_sql("health_income", conn, if_exists="replace", index=False)
    count = pd.read_sql("SELECT COUNT(*) as total FROM health_income", conn).iloc[0]["total"]
    print(f"   ✅ {count:,} rows loaded into health_income table")


def verify_data(conn: sqlite3.Connection):
    """Run a quick verification query."""
    print("\n🔍 Quick verification:")
    result = pd.read_sql("""
        SELECT 
            income_quartile,
            ROUND(AVG(life_expectancy), 2) AS avg_life_expectancy,
            COUNT(*) AS county_count
        FROM health_income
        GROUP BY income_quartile
        ORDER BY income_quartile
    """, conn)
    print(result.to_string(index=False))


def run():
    """Run the full database loading pipeline."""
    if not os.path.exists(CLEANED_DATA_PATH):
        print(f"❌ Cleaned data not found at {CLEANED_DATA_PATH}")
        print("   Please run src/data_loader.py first")
        return

    df = pd.read_csv(CLEANED_DATA_PATH)
    conn = sqlite3.connect(DB_PATH)

    create_database(conn)
    load_data_to_db(conn, df)
    verify_data(conn)

    conn.close()
    print(f"\n✅ Database saved to {DB_PATH}")
    print("   Connect Power BI or Tableau to this file to build your dashboards!")


if __name__ == "__main__":
    run()
