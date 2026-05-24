# EDA Run Results

I ran the EDA workflow for the Penguins dataset successfully. The script loaded the dataset, inspected the data structure, checked for missing values and duplicates, created a cleaned DataFrame, calculated descriptive statistics, computed a correlation matrix, and generated visualizations.

## Run Environment

- Project: Exploratory Data Analysis (EDA) - Penguins
- Repository: `datafun-04-notebooks`
- Python version: 3.14.2
- Operating system: Windows 11
- Shell: PowerShell
- Dataset source: Seaborn Penguins dataset

### Dataset Overview

The Penguins dataset loaded successfully with:

- 344 rows
- 7 columns

The columns in the dataset are:

- `species`
- `island`
- `bill_length_mm`
- `bill_depth_mm`
- `flipper_length_mm`
- `body_mass_g`
- `sex`

### Data Quality Findings

The data quality check showed that the dataset had some missing values but no duplicate rows.

Missing values included:

- `sex`: 11 missing values
- `bill_length_mm`: 2 missing values
- `bill_depth_mm`: 2 missing values
- `flipper_length_mm`: 2 missing values
- `body_mass_g`: 2 missing values

Duplicate rows detected:

- 0 duplicate rows

After dropping rows with missing values in the key numeric and grouping fields, the cleaned dataset had:

- 342 rows
- 7 columns

### Descriptive Statistics

The numeric columns analyzed were:

- `bill_length_mm`
- `bill_depth_mm`
- `flipper_length_mm`
- `body_mass_g`

The overall descriptive statistics showed the following:

- Average bill length: about 43.92 mm
- Average bill depth: about 17.15 mm
- Average flipper length: about 200.92 mm
- Average body mass: about 4201.75 g

The grouped statistics by species showed clear differences among Adelie, Chinstrap, and Gentoo penguins. Gentoo penguins had the highest average flipper length and body mass compared with the other species.

### Correlation Findings

The correlation matrix showed several interesting relationships:

- `flipper_length_mm` and `body_mass_g` had a strong positive correlation of about 0.87.
- `bill_length_mm` and `flipper_length_mm` had a positive correlation of about 0.66.
- `bill_depth_mm` and `flipper_length_mm` had a negative correlation of about -0.58.
- `bill_depth_mm` and `body_mass_g` had a negative correlation of about -0.47.

These results suggest that penguins with longer flippers tend to have greater body mass. The results also show that bill depth does not increase in the same way as flipper length or body mass.

### Visualizations Created

The script created two chart windows using Matplotlib and Seaborn:

1. A scatter plot showing flipper length vs. bill length by species.
2. A box plot showing flipper length by species.

The scatter plot helped show how penguin species cluster based on flipper length and bill length. The box plot helped compare flipper length distributions across species.

### Key Insights

This EDA workflow showed that the Penguins dataset contains useful patterns for comparing species. Gentoo penguins appear to be larger on average, especially in flipper length and body mass. The visualizations made the species differences easier to understand than looking at tables alone.

This project helped me practice important exploratory data analysis skills, including loading data, inspecting structure, checking data quality, cleaning data, calculating statistics, analyzing correlations, and creating visualizations.

## Project Visualizations

### Flipper Length by Species

This box plot compares flipper length across the Adelie, Chinstrap, and Gentoo penguin species.

![Flipper Length by Species](artifacts/flipper_length_by_species.png)

### Flipper Length vs Bill Length by Species

This scatter plot shows the relationship between flipper length and bill length, grouped by penguin species.

![Flipper Length vs Bill Length](artifacts/flipper_length_vs_bill_length_by_species.png)

## Penguins CSV

Alternative: Load from CSV file instead of seaborn.

Download penguins.csv from: <https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv>

Save it to project data/raw folder.

NOTE: The CSV file is not exactly the same as the Seaborn version.

- CSV includes a `year` column (2007, 2008, 2009)
- Seaborn version does not include `year`

It is included here for visual inspection and/or opening in Excel as you like.

### Run Log Summary

```text
2026-05-24 13:28:09 | INFO | EDA | === RUN START ===
2026-05-24 13:28:09 | INFO | EDA | project=Exploratory Data Analysis (EDA) - Penguins
2026-05-24 13:28:09 | INFO | EDA | repo_dir=datafun-04-notebooks
2026-05-24 13:28:09 | INFO | EDA | python=3.14.2
2026-05-24 13:28:09 | INFO | EDA | os=Windows 11
2026-05-24 13:28:09 | INFO | EDA | shell=powershell
2026-05-24 13:28:09 | INFO | EDA | Data loaded: 344 rows, 7 columns
2026-05-24 13:28:10 | INFO | EDA | Duplicate rows detected: 0
2026-05-24 13:28:10 | INFO | EDA | Cleaned view shape: 342 rows, 7 columns
2026-05-24 13:28:10 | INFO | EDA | Computing overall descriptive statistics
2026-05-24 13:28:10 | INFO | EDA | Computing descriptive statistics by species
2026-05-24 13:28:10 | INFO | EDA | Computing correlation matrix for numeric columns
2026-05-24 13:28:10 | INFO | EDA | Creating scatter plot: flipper length vs bill length
2026-05-24 14:02:47 | INFO | EDA | EDA workflow complete
