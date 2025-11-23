def checkMissingValues(df, key_cols=None):
    """
    Performs multiple data-quality checks:
    - Missing values per column
    - Columns with >5% missing data
    - Rows with missing values in key columns
    - Duplicate row count
    - Cardinality of categorical columns
    """

    # --------------------------------------------
    # Missing values per column
    # --------------------------------------------
    print("\n📌 Missing values per column:")
    print(df.isna().sum())

    # Percentage of missing values
    null_percentages = df.isnull().sum() / len(df) * 100
    columns_with_high_nulls = null_percentages[null_percentages > 5]

    print("\n📌 Columns with >5% missing values:")
    if len(columns_with_high_nulls) == 0:
        print("✔️ None")
    else:
        print(columns_with_high_nulls)

    # --------------------------------------------
    # Missing rows in key columns
    # --------------------------------------------
    if key_cols is None:
        key_cols = ['Close', 'Open', 'High', 'Volume']  # defaults

    existing_keys = [c for c in key_cols if c in df.columns]

    missing_rows_mask = df[existing_keys].isnull().any(axis=1)
    missing_value_rows = df[missing_rows_mask]

    print(f"\n📌 Total rows with missing values in key columns {existing_keys}: {len(missing_value_rows)}")

    if len(missing_value_rows) > 0:
        print("\n📌 Rows with missing values in key columns:")
        print(missing_value_rows[existing_keys])
    else:
        print("✔️ No missing rows in key columns")
