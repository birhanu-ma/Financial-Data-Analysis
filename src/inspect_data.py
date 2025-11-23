def inspectData(df):
    """
    Logs basic information about the dataset:
    - Shape
    - First 5 rows
    - Last 5 rows
    - 5 random sample rows
    - DataFrame info
    """
    print(f"\n📌 Dataset Shape: {df.shape}\n")

    print("📌 First 5 rows:")
    display(df.head())

    print("\n📌 Last 5 rows:")
    display(df.tail())

    print("\n📌 Random 5 rows:")
    display(df.sample(5))

    print("\n📌 DataFrame Info:")
    df.info()
