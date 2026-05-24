# Custom Project

## Dataset

For my custom project, I used the Seaborn Penguins dataset. This dataset contains measurements for penguins from the Palmer Archipelago in Antarctica.

The dataset includes records with fields such as:

- `species`
- `island`
- `bill_length_mm`
- `bill_depth_mm`
- `flipper_length_mm`
- `body_mass_g`
- `sex`

Each row represents one penguin. The dataset is useful for exploratory data analysis because it includes both categorical fields, such as species and island, and numeric measurement fields, such as bill length, flipper length, and body mass.

I used the original Penguins dataset from Seaborn and then created a cleaned view by dropping rows with missing values in the key numeric columns and the species column.

### Signals

The original signals used in this project were the penguin measurement fields:

- `bill_length_mm`
- `bill_depth_mm`
- `flipper_length_mm`
- `body_mass_g`

These signals helped compare penguin size and body structure across different species and islands.

I also created new signals as part of my technical modification:

- `body_mass_kg`
- `flipper_body_ratio`
- `size_category`

The `body_mass_kg` signal converts body mass from grams to kilograms, making the measurement easier to interpret.

The `flipper_body_ratio` signal compares flipper length to body mass. This helps show the relationship between a penguin’s flipper length and overall body size.

The `size_category` signal classifies penguins as small, medium, or large based on body mass. This turns a numeric measurement into a category that can be used for easier comparison.

### Experiments

For my technical modification, I changed the original EDA workflow by adding engineered fields to the Penguins dataset.

The original example loaded the data, inspected the dataset, checked for missing values, calculated descriptive statistics, created a correlation matrix, and made basic plots.

My modification added new calculated fields:

- `body_mass_kg`
- `flipper_body_ratio`
- `size_category`

I also added code to save visualizations and summary tables to the `artifacts/` folder. This made the project easier to share on GitHub and allowed the charts to be used in the README file.

For the new problem, I applied the EDA skills to a wildlife research question: comparing penguin body size patterns by species and island.

I created summaries that show:

- penguin count by species
- average body mass by species
- average body mass by island
- average flipper length by species
- average flipper length by island
- average flipper-to-body ratio by species

I also created new charts to compare average body mass by species and island.

### Results

After running the project, the Penguins dataset loaded successfully. The dataset contained 344 rows and 7 columns before cleaning.

The data quality check showed that some columns had missing values. The `sex` column had the most missing values, and some numeric measurement columns also had missing values. There were no duplicate rows detected.

After cleaning the dataset by dropping rows with missing values in the important numeric and grouping columns, the cleaned dataset had 342 rows.

The descriptive statistics showed that Gentoo penguins generally had the highest average flipper length and body mass compared with Adelie and Chinstrap penguins.

The correlation matrix showed a strong positive relationship between `flipper_length_mm` and `body_mass_g`. This means penguins with longer flippers also tended to have higher body mass.

The project created and saved several artifacts, including:

- `flipper_vs_bill_length_by_species.png`
- `flipper_length_by_species.png`
- `average_body_mass_by_species.png`
- `average_body_mass_by_island.png`
- `species_size_summary.csv`
- `island_size_summary.csv`

The charts helped visually confirm the patterns in the data. Gentoo penguins appeared larger overall, especially in body mass and flipper length.

### Interpretation

This project showed how exploratory data analysis can turn a dataset into useful insights. The original Penguins dataset provided raw measurements, but the cleaning, summaries, engineered fields, and visualizations helped make the patterns easier to understand.

The technical modification improved the analysis by creating new signals. Instead of only looking at body mass in grams, I converted it to kilograms, created a flipper-to-body ratio, and grouped penguins into size categories. These changes made the data more meaningful and easier to compare.

The business intelligence gained from this project is that species and island are important grouping fields when analyzing penguin body size patterns. Gentoo penguins had the highest average body mass and flipper length, which suggests they are generally larger than the other species in the dataset.

If this were used in a real wildlife research system, the analysis could help researchers compare animal populations, identify physical differences between groups, and communicate findings through charts and summary tables.

Overall, this custom project helped me practice loading data, checking data quality, cleaning data, engineering new fields, creating visualizations, saving artifacts, and interpreting results from an analyst perspective.

## Data Analytics Fundamentals

> Professional Python for Data Analytics

This project comes with professional documentation.

Explore the tabs and sidebars for content.

This is where we present our analytics work.

See:

- [Resources](./RESOURCES.md)
- [Troubleshooting](./TROUBLESHOOTING.md)

---

To customize, modify:

- `docs/` (folder with Markdown files)
- `mkdocs.yaml` (in the root project folder)
  - scroll to the end for th
