# fin-dash

This repository contains an interactive financial dashboard in Python using Dash.

> Note: This dashboard is a work-in-progress and all data is fictitious, created purely for learning and experimentation. This README mainly serves as a development reference to guide the structure and components of the dashboard.

## Columns Reference

| Column    | Type      | Usage in the Dashboard                       |
| --------- | --------- | -------------------------------------------- |
| `month`   | datetime  | Line chart (revenue, expense, profit trends) |
| `product` | string    | Bar or pie chart (compare products)          |
| `region`  | string    | Filters or heatmaps (regional analysis)      |
| `revenue` | int/float | KPI, line, bar, totals                       |
| `expense` | int/float | KPI, line, bar, totals                       |
| `profit`  | int/float | KPI, line, bar, heatmap, margin              |


## How to use these columns in the dashboard:

- KPIs: Sum revenue, expense, and profit by period, product, or region.

- Line chart: Monthly evolution of revenue, expense, and profit.

- Bar chart: Revenue by product or region.

- Pie chart: Share of each product in total revenue.

- Heatmap: Revenue or profit by product (row) and region (column).

- Filters: By month, product, or region.

## Dashboard Components Reference

- KPIs (Key Metrics) – Highlight key metrics at the top of the dashboard.

- Line Chart (Time Series) – Track metric evolution over time.

- Bar Chart – Compare categories or products.

- Pie / Donut Chart – Show percentage distributions.

- Heatmaps / Conditional Tables – Visual emphasis on values.

- Waterfall / Funnel Charts – Track flows or conversions.

- Filters & Interactivity – Make the dashboard dynamic and explorable.

## Layout Notes (for development reference)

- Top: 3–4 prominent KPIs

- Middle: Line + bar charts for trends and comparisons

- Side / bottom: Pie, heatmap, or table for detailed analysis

- Filters: Top or side, to allow exploration