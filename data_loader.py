"""
data_loader.py
--------------
Step 1 of the pipeline: Load, clean, and merge CDC + Census data.
Output: cleaned CSV saved to data/cleaned_health_income.csv
"""

import pandas as pd
import numpy as np
import os

RAW_CDC_PATH = "data/cdc_life_expectancy.csv"
RAW_CENSUS_PATH = "data/census_income.csv"
OUTPUT_PATH = "data/cleaned_health_income.csv"


def load_cdc_data(path: str) -> pd.DataFrame:
    """Load and clean CDC life expectancy data."""
    print("📥 Loading CDC life expectancy data...")
    df = pd.read_csv(path)

    # Standardize column names (lowercase, no spaces)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Keep only relevant columns — adjust names to match your downloaded file
    df = df.rename(columns={
        "county_code": "fips",
        "life_expectancy": "life_expectancy",
        "state": "state",
        "county": "county_name",
    })

    df = df[["fips", "state", "county_name", "life_expectancy"]].dropna()
    df["fips"] = df["fips"].astype(str).str.zfill(5)
    df["life_expectancy"] = pd.to_numeric(df["life_expectancy"], errors="coerce")

    print(f"   ✅ {len(df):,} counties loaded from CDC")
    return df


def load_census_data(path: str) -> pd.DataFrame:
    """Load and clean Census median household income data."""
    print("📥 Loading Census income data...")
    df = pd.read_csv(path, encoding="latin1")

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Rename to standard names — adjust to match your downloaded file
    df = df.rename(columns={
        "geo_id": "fips",
        "median_household_income": "median_income",
        "state": "state",
    })

    df = df[["fips", "median_income"]].dropna()
    df["fips"] = df["fips"].astype(str).str.zfill(5).str[-5:]  # Keep last 5 digits
    df["median_income"] = pd.to_numeric(
        df["median_income"].astype(str).str.replace(",", "").str.replace("$", ""),
        errors="coerce"
    )

    print(f"   ✅ {len(df):,} counties loaded from Census")
    return df


def merge_and_enrich(cdc_df: pd.DataFrame, census_df: pd.DataFrame) -> pd.DataFrame:
    """Merge CDC and Census data on FIPS code, add derived columns."""
    print("🔗 Merging datasets...")
    df = pd.merge(cdc_df, census_df, on="fips", how="inner")

    # Income quartile buckets
    df["income_quartile"] = pd.qcut(
        df["median_income"],
        q=4,
        labels=["Q1 (Lowest)", "Q2", "Q3", "Q4 (Highest)"]
    )

    # Income group (simplified)
    df["income_group"] = pd.cut(
        df["median_income"],
        bins=[0, 35000, 55000, 75000, float("inf")],
        labels=["Low (<$35k)", "Middle ($35k-$55k)", "Upper-Mid ($55k-$75k)", "High (>$75k)"]
    )

    print(f"   ✅ Merged dataset: {len(df):,} counties")
    return df


def run():
    """Run the full data loading pipeline."""
    if not os.path.exists(RAW_CDC_PATH):
        print(f"❌ CDC file not found at {RAW_CDC_PATH}")
        print("   Please follow instructions in data/README.md")
        return

    if not os.path.exists(RAW_CENSUS_PATH):
        print(f"❌ Census file not found at {RAW_CENSUS_PATH}")
        print("   Please follow instructions in data/README.md")
        return

    cdc_df = load_cdc_data(RAW_CDC_PATH)
    census_df = load_census_data(RAW_CENSUS_PATH)
    merged_df = merge_and_enrich(cdc_df, census_df)

    merged_df.to_csv(OUTPUT_PATH, index=False)
    print(f"\n✅ Cleaned data saved to {OUTPUT_PATH}")
    print(merged_df.head())


if __name__ == "__main__":
    run()
