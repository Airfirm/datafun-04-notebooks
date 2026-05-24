"""app_femi.py - Custom Penguins EDA project.

Author: Oluwafemi Salawu
Date: 2026-05

Purpose:
- Perform exploratory data analysis (EDA) on the penguins dataset.
- Make a technical modification by adding engineered fields.
- Apply the skills to a new problem: comparing penguin body size patterns.
- Save chart images and summary tables to the artifacts folder.

Data Source:
- Palmer Archipelago penguin data
- Available through Seaborn

Technical Modification:
- Adds body_mass_kg
- Adds flipper_body_ratio
- Adds size_category
- Saves charts to artifacts/

New Problem:
- Helps a wildlife researcher compare penguin body size patterns by species and island.
"""

# === Section 1a. Imports ===

import logging
from pathlib import Path

from datafun_toolkit.logger import get_logger, log_header
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# === Section 1b. Configure Logger ===

LOG: logging.Logger = get_logger("EDA", level="DEBUG")

# === Section 1c. Global Constants and Configuration ===

NUMERIC_COLS = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
]

GROUP_COL = "species"

ROOT_DIR = Path.cwd()
ARTIFACTS_DIR = ROOT_DIR / "artifacts"

SCATTER_PLOT_PATH = ARTIFACTS_DIR / "flipper_vs_bill_length_by_species.png"
BOX_PLOT_PATH = ARTIFACTS_DIR / "flipper_length_by_species.png"
SPECIES_BODY_MASS_PATH = ARTIFACTS_DIR / "average_body_mass_by_species.png"
ISLAND_BODY_MASS_PATH = ARTIFACTS_DIR / "average_body_mass_by_island.png"
SPECIES_SUMMARY_PATH = ARTIFACTS_DIR / "species_size_summary.csv"
ISLAND_SUMMARY_PATH = ARTIFACTS_DIR / "island_size_summary.csv"

# Pandas display configuration
pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 120)


# === Section 2. Load the Data ===


def load_data() -> pd.DataFrame:
    """Load the Penguins dataset from Seaborn.

    Returns:
        pd.DataFrame: Penguins dataset.
    """
    LOG.info("Loading penguins dataset from seaborn")
    df = sns.load_dataset("penguins")
    LOG.info("Data loaded: %s rows, %s columns", df.shape[0], df.shape[1])
    return df


# === Section 3. Understand Data Shape and Basic Structure ===


def inspect_basic(df: pd.DataFrame) -> None:
    """Inspect the basic structure of the dataset.

    Args:
        df: Penguins DataFrame.
    """
    LOG.info("Inspecting first rows of data")
    LOG.debug("\n%s", df.head())

    LOG.info("Column names")
    LOG.debug("%s", list(df.columns))

    LOG.info("DataFrame info")
    df.info()

    LOG.info("Dataset shape: %s rows, %s columns", df.shape[0], df.shape[1])


# === Section 4. Check for Missing Data ===


def build_data_dictionary(df: pd.DataFrame) -> pd.DataFrame:
    """Build a starter data dictionary.

    Args:
        df: Penguins DataFrame.

    Returns:
        pd.DataFrame: Data dictionary with column names, data types,
        missing counts, and missing percentages.
    """
    LOG.info("Building starter data dictionary")

    data_dictionary = pd.DataFrame(
        {
            "column": df.columns,
            "dtype": [str(t) for t in df.dtypes],
            "missing_count": df.isna().sum().values,
            "missing_pct": (df.isna().mean() * 100).round(2).values,
        }
    )

    LOG.debug("\n%s", data_dictionary)
    return data_dictionary


def check_quality(df: pd.DataFrame) -> None:
    """Perform basic data quality checks.

    Args:
        df: Penguins DataFrame.
    """
    LOG.info("Checking missing values per column")
    LOG.debug("\n%s", df.isna().sum().sort_values(ascending=False))

    dup_count = int(df.duplicated().sum())
    LOG.info("Duplicate rows detected: %s", dup_count)

    LOG.info("Basic sanity check for numeric columns")
    LOG.debug("\n%s", df[NUMERIC_COLS].describe())


# === Section 5. Optional Cleaning Step ===


def make_clean_view(df: pd.DataFrame) -> pd.DataFrame:
    """Create a cleaned view for EDA.

    The original DataFrame is unchanged. Rows with missing values
    in key numeric columns or the grouping column are removed.

    Args:
        df: Penguins DataFrame.

    Returns:
        pd.DataFrame: Cleaned copy of the data.
    """
    LOG.info("Creating cleaned view for EDA")
    df_clean = df.dropna(subset=NUMERIC_COLS + [GROUP_COL]).copy()

    LOG.info(
        "Cleaned view shape: %s rows, %s columns",
        df_clean.shape[0],
        df_clean.shape[1],
    )

    return df_clean


# === Section 6. Descriptive Statistics ===


def descriptive_stats(df_clean: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Compute descriptive statistics overall and by species.

    Args:
        df_clean: Cleaned Penguins DataFrame.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: Overall stats and grouped stats.
    """
    LOG.info("Computing overall descriptive statistics")
    stats_overall = df_clean[NUMERIC_COLS].describe().T
    LOG.debug("\n%s", stats_overall)

    LOG.info("Computing descriptive statistics by species")
    stats_by_species = df_clean.groupby(GROUP_COL)[NUMERIC_COLS].agg(
        ["count", "mean", "std", "min", "max"]
    )
    LOG.debug("\n%s", stats_by_species)

    return stats_overall, stats_by_species


# === Section 7. Correlation Matrix ===


def correlation_matrix(df_clean: pd.DataFrame) -> pd.DataFrame:
    """Compute a numeric correlation matrix.

    Args:
        df_clean: Cleaned Penguins DataFrame.

    Returns:
        pd.DataFrame: Correlation matrix.
    """
    LOG.info("Computing correlation matrix for numeric columns")
    corr = df_clean[NUMERIC_COLS].corr()
    LOG.debug("\n%s", corr)
    return corr


# === Section 8. Phase 4 Technical Modification ===


def add_engineered_fields(df_clean: pd.DataFrame) -> pd.DataFrame:
    """Add engineered fields for deeper analysis.

    Technical modification:
    - Convert body mass from grams to kilograms.
    - Calculate flipper-to-body ratio.
    - Classify penguins into size categories.

    Args:
        df_clean: Cleaned Penguins DataFrame.

    Returns:
        pd.DataFrame: DataFrame with added engineered fields.
    """
    LOG.info("Adding engineered fields")

    df_features = df_clean.copy()

    df_features["body_mass_kg"] = (df_features["body_mass_g"] / 1000).round(2)

    df_features["flipper_body_ratio"] = (
        df_features["flipper_length_mm"] / df_features["body_mass_g"]
    ).round(4)

    df_features["size_category"] = pd.cut(
        df_features["body_mass_g"],
        bins=[0, 3500, 4500, float("inf")],
        labels=["small", "medium", "large"],
    )

    LOG.info("Engineered fields added: body_mass_kg, flipper_body_ratio, size_category")
    LOG.debug(
        "\n%s",
        df_features[
            [
                "species",
                "island",
                "flipper_length_mm",
                "body_mass_g",
                "body_mass_kg",
                "flipper_body_ratio",
                "size_category",
            ]
        ].head(),
    )

    return df_features


# === Section 9. Phase 5 Apply Skills to a New Problem ===


def summarize_size_patterns(
    df_features: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Summarize penguin body size patterns by species and island.

    New problem:
    Help a wildlife researcher compare penguin body size patterns.

    Args:
        df_features: Penguins DataFrame with engineered fields.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: Species summary and island summary.
    """
    LOG.info("Summarizing body size patterns by species")

    species_size_summary = (
        df_features.groupby("species", observed=True)
        .agg(
            penguin_count=("species", "count"),
            avg_body_mass_g=("body_mass_g", "mean"),
            avg_body_mass_kg=("body_mass_kg", "mean"),
            avg_flipper_length_mm=("flipper_length_mm", "mean"),
            avg_flipper_body_ratio=("flipper_body_ratio", "mean"),
        )
        .round(2)
        .reset_index()
    )

    LOG.debug("\n%s", species_size_summary)

    LOG.info("Summarizing body size patterns by island")

    island_size_summary = (
        df_features.groupby("island", observed=True)
        .agg(
            penguin_count=("island", "count"),
            avg_body_mass_g=("body_mass_g", "mean"),
            avg_body_mass_kg=("body_mass_kg", "mean"),
            avg_flipper_length_mm=("flipper_length_mm", "mean"),
        )
        .round(2)
        .reset_index()
    )

    LOG.debug("\n%s", island_size_summary)

    return species_size_summary, island_size_summary


def log_analyst_insights(
    species_size_summary: pd.DataFrame,
    island_size_summary: pd.DataFrame,
) -> None:
    """Log analyst insights from the new problem analysis.

    Args:
        species_size_summary: Summary table grouped by species.
        island_size_summary: Summary table grouped by island.
    """
    top_species = species_size_summary.sort_values(
        by="avg_body_mass_g",
        ascending=False,
    ).iloc[0]

    top_island = island_size_summary.sort_values(
        by="avg_body_mass_g",
        ascending=False,
    ).iloc[0]

    LOG.info("Analyst Insights")
    LOG.info(
        "The species with the highest average body mass is %s "
        "with an average body mass of %.2f grams.",
        top_species["species"],
        top_species["avg_body_mass_g"],
    )
    LOG.info(
        "The island with the highest average body mass is %s "
        "with an average body mass of %.2f grams.",
        top_island["island"],
        top_island["avg_body_mass_g"],
    )
    LOG.info(
        "These results suggest that species and island location are useful "
        "grouping fields for understanding penguin body size patterns."
    )


# === Section 10. Create and Save Plots ===


def make_original_plots(df_features: pd.DataFrame) -> None:
    """Create and save the original EDA plots.

    Args:
        df_features: Penguins DataFrame with engineered fields.
    """
    LOG.info("Creating scatter plot: flipper length vs bill length")

    plt.figure(figsize=(8, 6))

    scatter_plt: Axes = sns.scatterplot(
        data=df_features,
        x="flipper_length_mm",
        y="bill_length_mm",
        hue=GROUP_COL,
    )

    scatter_plt.set_xlabel("Flipper length (mm)")
    scatter_plt.set_ylabel("Bill length (mm)")
    scatter_plt.set_title("Flipper Length vs Bill Length by Species")

    plt.tight_layout()
    plt.savefig(SCATTER_PLOT_PATH)
    LOG.info("Saved chart to: %s", SCATTER_PLOT_PATH)

    plt.figure(figsize=(8, 6))

    box_plt: Axes = sns.boxplot(
        data=df_features,
        x=GROUP_COL,
        y="flipper_length_mm",
    )

    box_plt.set_xlabel("Species")
    box_plt.set_ylabel("Flipper length (mm)")
    box_plt.set_title("Flipper Length by Species")

    plt.tight_layout()
    plt.savefig(BOX_PLOT_PATH)
    LOG.info("Saved chart to: %s", BOX_PLOT_PATH)


def make_new_problem_plots(
    species_size_summary: pd.DataFrame,
    island_size_summary: pd.DataFrame,
) -> None:
    """Create and save plots for the new analysis problem.

    Args:
        species_size_summary: Summary table grouped by species.
        island_size_summary: Summary table grouped by island.
    """
    LOG.info("Creating bar chart: average body mass by species")

    plt.figure(figsize=(8, 6))

    species_bar: Axes = sns.barplot(
        data=species_size_summary,
        x="species",
        y="avg_body_mass_g",
    )

    species_bar.set_xlabel("Species")
    species_bar.set_ylabel("Average body mass (g)")
    species_bar.set_title("Average Body Mass by Species")

    plt.tight_layout()
    plt.savefig(SPECIES_BODY_MASS_PATH)
    LOG.info("Saved chart to: %s", SPECIES_BODY_MASS_PATH)

    LOG.info("Creating bar chart: average body mass by island")

    plt.figure(figsize=(8, 6))

    island_bar: Axes = sns.barplot(
        data=island_size_summary,
        x="island",
        y="avg_body_mass_g",
    )

    island_bar.set_xlabel("Island")
    island_bar.set_ylabel("Average body mass (g)")
    island_bar.set_title("Average Body Mass by Island")

    plt.tight_layout()
    plt.savefig(ISLAND_BODY_MASS_PATH)
    LOG.info("Saved chart to: %s", ISLAND_BODY_MASS_PATH)


# === Section 11. Save Artifacts ===


def save_summary_tables(
    species_size_summary: pd.DataFrame,
    island_size_summary: pd.DataFrame,
) -> None:
    """Save summary tables to CSV files.

    Args:
        species_size_summary: Summary table grouped by species.
        island_size_summary: Summary table grouped by island.
    """
    LOG.info("Saving summary tables")

    species_size_summary.to_csv(SPECIES_SUMMARY_PATH, index=False)
    island_size_summary.to_csv(ISLAND_SUMMARY_PATH, index=False)

    LOG.info("Saved species summary to: %s", SPECIES_SUMMARY_PATH)
    LOG.info("Saved island summary to: %s", ISLAND_SUMMARY_PATH)


def initialize_artifacts_folder() -> None:
    """Create the artifacts folder if it does not already exist."""
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    LOG.info("Artifacts folder ready: %s", ARTIFACTS_DIR)


# === Section 12. Main Function ===


def main() -> None:
    """Run the complete EDA workflow."""
    log_header(LOG, "Exploratory Data Analysis (EDA) - Penguins")

    LOG.info("Section 1: Setup")
    initialize_artifacts_folder()

    LOG.info("Section 2: Load the data")
    df = load_data()

    LOG.info("Section 3: Inspect data shape and basic structure")
    inspect_basic(df)

    LOG.info("Section 4: Check data quality")
    data_dictionary = build_data_dictionary(df)
    LOG.debug("\n%s", data_dictionary)
    check_quality(df)

    LOG.info("Section 5: Create a cleaned view for EDA")
    df_clean = make_clean_view(df)

    LOG.info("Section 6: Compute descriptive statistics")
    stats_overall, stats_by_species = descriptive_stats(df_clean)
    LOG.debug("\n%s", stats_overall)
    LOG.debug("\n%s", stats_by_species)

    LOG.info("Section 7: Compute correlation matrix")
    corr = correlation_matrix(df_clean)
    LOG.debug("\n%s", corr)

    LOG.info("Section 8: Phase 4 Technical Modification")
    df_features = add_engineered_fields(df_clean)

    LOG.info("Section 9: Phase 5 Apply Skills to a New Problem")
    species_size_summary, island_size_summary = summarize_size_patterns(df_features)
    log_analyst_insights(species_size_summary, island_size_summary)

    LOG.info("Section 10: Create and save plots")
    make_original_plots(df_features)
    make_new_problem_plots(species_size_summary, island_size_summary)

    LOG.info("Section 11: Save summary tables")
    save_summary_tables(species_size_summary, island_size_summary)

    LOG.info("EDA workflow complete")
    LOG.info("Artifacts saved in: %s", ARTIFACTS_DIR)
    LOG.info("Charts and CSV summary files are ready for GitHub.")

    plt.show()


# === Conditional Execution Guard ===

if __name__ == "__main__":
    main()
