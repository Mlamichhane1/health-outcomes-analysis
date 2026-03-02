-- schema.sql
-- Creates the SQLite database tables for the Health Outcomes & Income project

DROP TABLE IF EXISTS health_income;

CREATE TABLE health_income (
    fips            TEXT PRIMARY KEY,   -- 5-digit county FIPS code
    state           TEXT,               -- State name
    county_name     TEXT,               -- County name
    life_expectancy REAL,               -- Average life expectancy (years)
    median_income   REAL,               -- Median household income ($)
    income_quartile TEXT,               -- Q1 (Lowest) to Q4 (Highest)
    income_group    TEXT                -- Low / Middle / Upper-Mid / High
);
