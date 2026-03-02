-- queries.sql
-- Key business analysis queries for the Health Outcomes & Income project
-- Run these in SQLite, Power BI, or Tableau to power your dashboards


-- ─────────────────────────────────────────────────────────────────────────────
-- 1. NATIONAL OVERVIEW
-- Average life expectancy and income across all counties
-- ─────────────────────────────────────────────────────────────────────────────
SELECT
    COUNT(*)                            AS total_counties,
    ROUND(AVG(life_expectancy), 2)      AS avg_life_expectancy,
    ROUND(AVG(median_income), 0)        AS avg_median_income,
    ROUND(MIN(life_expectancy), 2)      AS min_life_expectancy,
    ROUND(MAX(life_expectancy), 2)      AS max_life_expectancy
FROM health_income;


-- ─────────────────────────────────────────────────────────────────────────────
-- 2. LIFE EXPECTANCY BY INCOME QUARTILE
-- Core finding: do richer counties live longer?
-- ─────────────────────────────────────────────────────────────────────────────
SELECT
    income_quartile,
    ROUND(AVG(life_expectancy), 2)  AS avg_life_expectancy,
    ROUND(AVG(median_income), 0)    AS avg_median_income,
    COUNT(*)                        AS county_count
FROM health_income
WHERE income_quartile IS NOT NULL
GROUP BY income_quartile
ORDER BY income_quartile;


-- ─────────────────────────────────────────────────────────────────────────────
-- 3. TOP 10 COUNTIES — HIGHEST LIFE EXPECTANCY
-- ─────────────────────────────────────────────────────────────────────────────
SELECT
    county_name,
    state,
    ROUND(life_expectancy, 2)   AS life_expectancy,
    ROUND(median_income, 0)     AS median_income,
    income_quartile
FROM health_income
ORDER BY life_expectancy DESC
LIMIT 10;


-- ─────────────────────────────────────────────────────────────────────────────
-- 4. BOTTOM 10 COUNTIES — LOWEST LIFE EXPECTANCY
-- ─────────────────────────────────────────────────────────────────────────────
SELECT
    county_name,
    state,
    ROUND(life_expectancy, 2)   AS life_expectancy,
    ROUND(median_income, 0)     AS median_income,
    income_quartile
FROM health_income
ORDER BY life_expectancy ASC
LIMIT 10;


-- ─────────────────────────────────────────────────────────────────────────────
-- 5. STATE-LEVEL SUMMARY
-- Average life expectancy and income per state (for map visualizations)
-- ─────────────────────────────────────────────────────────────────────────────
SELECT
    state,
    ROUND(AVG(life_expectancy), 2)  AS avg_life_expectancy,
    ROUND(AVG(median_income), 0)    AS avg_median_income,
    COUNT(*)                        AS county_count
FROM health_income
GROUP BY state
ORDER BY avg_life_expectancy DESC;


-- ─────────────────────────────────────────────────────────────────────────────
-- 6. INCOME-HEALTH GAP BY STATE
-- States with the largest life expectancy gap between richest and poorest counties
-- ─────────────────────────────────────────────────────────────────────────────
SELECT
    state,
    ROUND(MAX(life_expectancy) - MIN(life_expectancy), 2)   AS life_expectancy_gap,
    ROUND(MAX(median_income) - MIN(median_income), 0)       AS income_gap,
    COUNT(*)                                                AS county_count
FROM health_income
GROUP BY state
HAVING county_count >= 5       -- Only states with enough counties for fair comparison
ORDER BY life_expectancy_gap DESC
LIMIT 15;


-- ─────────────────────────────────────────────────────────────────────────────
-- 7. INCOME GROUP BREAKDOWN
-- Life expectancy across Low / Middle / Upper-Mid / High income groups
-- ─────────────────────────────────────────────────────────────────────────────
SELECT
    income_group,
    ROUND(AVG(life_expectancy), 2)  AS avg_life_expectancy,
    ROUND(MIN(life_expectancy), 2)  AS min_life_expectancy,
    ROUND(MAX(life_expectancy), 2)  AS max_life_expectancy,
    COUNT(*)                        AS county_count
FROM health_income
WHERE income_group IS NOT NULL
GROUP BY income_group
ORDER BY avg_life_expectancy DESC;


-- ─────────────────────────────────────────────────────────────────────────────
-- 8. FULL DATASET — for Power BI / Tableau connection
-- ─────────────────────────────────────────────────────────────────────────────
SELECT *
FROM health_income
ORDER BY state, county_name;
