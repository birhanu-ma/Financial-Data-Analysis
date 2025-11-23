import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt   # <-- needed for plotting
import talib                      # <-- needed for indicators


class StockData:
    """
    Class to handle stock data loading, inspection, and quality checks.

    Attributes:
        ticker (str)       : Stock ticker symbol (e.g. "GOOG")
        start_date (str)   : Start date for data (YYYY-MM-DD)
        end_date (str)     : End date for data (YYYY-MM-DD)
        df (DataFrame)     : Pandas DataFrame holding stock data
    """

    def __init__(self, ticker, start_date="2009-01-01", end_date="2023-12-29"):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.df = pd.DataFrame()

    # -----------------------------
    # Load stock data
    # -----------------------------
    def load_data(self):
        """
        Loads historical stock data using yfinance.
        """
        self.df = yf.download(
            self.ticker,
            start=self.start_date,
            end=self.end_date,
            progress=False
        )
        if self.df.empty:
            print(f"⚠️ Warning: No data downloaded for {self.ticker}")
        return self.df

    # -----------------------------
    # Inspect dataset
    # -----------------------------
    def inspect_data(self):
        """
        Logs basic information about the dataset:
        - Shape
        - First 5 rows
        - Last 5 rows
        - 5 random sample rows
        - DataFrame info
        """
        if self.df.empty:
            print(f"⚠️ No data to inspect for {self.ticker}")
            return

        print(f"\n📌 Dataset Shape for {self.ticker}: {self.df.shape}\n")

        print("📌 First 5 rows:")
        display(self.df.head())

        print("\n📌 Last 5 rows:")
        display(self.df.tail())

        print("\n📌 Random 5 rows:")
        display(self.df.sample(5))

        print("\n📌 DataFrame Info:")
        self.df.info()

    # -----------------------------
    # Check missing values and data quality
    # -----------------------------
    def check_missing_values(self, key_cols=None):
        """
        Performs multiple data-quality checks:
        - Missing values per column
        - Columns with >5% missing data
        - Rows with missing values in key columns
        - Duplicate rows
        - Cardinality of categorical columns
        """

        if self.df.empty:
            print(f"⚠️ No data to check for {self.ticker}")
            return

        # Missing values per column
        print("\n📌 Missing values per column:")
        print(self.df.isna().sum())

        # Columns with >5% missing
        null_percentages = self.df.isnull().sum() / len(self.df) * 100
        high_null_cols = null_percentages[null_percentages > 5]

        print("\n📌 Columns with >5% missing values:")
        if high_null_cols.empty:
            print("✔️ None")
        else:
            print(high_null_cols)

        # Key columns
        if key_cols is None:
            key_cols = ['Close', 'Open', 'High', 'Volume']

        existing_keys = [c for c in key_cols if c in self.df.columns]
        missing_rows_mask = self.df[existing_keys].isnull().any(axis=1)
        missing_value_rows = self.df[missing_rows_mask]

        print(f"\n📌 Total rows with missing values in key columns {existing_keys}: {len(missing_value_rows)}")
        if len(missing_value_rows) > 0:
            print("\n📌 Rows with missing values in key columns:")
            display(missing_value_rows[existing_keys])
        else:
            print("✔️ No missing rows in key columns")

        # Duplicate rows
        dup_count = self.df.duplicated().sum()
        print(f"\n📌 Duplicate rows: {dup_count}")

        # Cardinality for categorical columns
        cat_cols = self.df.select_dtypes(include=["object", "category"]).columns.tolist()
        cardinality = {c: self.df[c].nunique() for c in cat_cols}
        print(f"\n📌 Cardinality (categoricals): {cardinality}")



    # -----------------------------
    # Indicator calculations
    # -----------------------------
    def calculate_sma(self, period=20):
        col_name = f"SMA_{period}"
        self.df[col_name] = talib.SMA(self.df["Close"].to_numpy().ravel(), timeperiod=period)

    def calculate_macd(self):
        macd, signal, hist = talib.MACD(self.df["Close"].to_numpy().ravel())
        self.df["MACD"] = macd
        self.df["MACD_signal"] = signal
        self.df["MACD_hist"] = hist

    def calculate_rsi(self, period=14):
        rsi_col = f"RSI_{period}"
        self.df[rsi_col] = talib.RSI(self.df["Close"].to_numpy().ravel(), timeperiod=period)

    # -----------------------------
    # Plotting
    # -----------------------------
    def plot_price(self):
        """Plots Close, Open, High, Low, and Volume charts."""
        df = self.df
        ticker = self.ticker

        df["Close"].plot(title=f"{ticker} Close Price")
        plt.ylabel("Price ($)")
        plt.show()

        df["Volume"].plot(title=f"{ticker} Daily Volume")
        plt.ylabel("Shares Traded")
        plt.show()

        df["High"].plot(title=f"{ticker} High Price")
        plt.ylabel("Price ($)")
        plt.show()

        df["Low"].plot(title=f"{ticker} Low Price")
        plt.ylabel("Price ($)")
        plt.show()

        df["Open"].plot(title=f"{ticker} Open Price")
        plt.ylabel("Price ($)")
        plt.show()

    def plot_price_sma(self):
        """Plots Close price with SMA20 and SMA50 if available."""
        df = self.df
        ticker = self.ticker

        fig, ax = plt.subplots(figsize=(14, 6))
        ax.plot(df.index, df["Close"], label="Price", color="black")

        if "SMA_20" in df.columns:
            ax.plot(df.index, df["SMA_20"], label="SMA 20", linestyle="--")
        if "SMA_50" in df.columns:
            ax.plot(df.index, df["SMA_50"], label="SMA 50", linestyle="-.")

        ax.set_title(f"{ticker} – Price & Moving Averages")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price ($)")
        ax.legend()
        plt.show()

    def plot_macd(self):
        """Plots MACD line, Signal line, and Histogram."""
        df = self.df
        ticker = self.ticker

        if "MACD" not in df.columns:
            self.calculate_macd()

        fig, ax = plt.subplots(figsize=(12, 4))
        ax.plot(df.index, df["MACD"], label="MACD", color="blue")
        ax.plot(df.index, df["MACD_signal"], label="Signal", color="orange")
        ax.bar(df.index, df["MACD_hist"], label="Histogram", color="gray")

        ax.set_title(f"{ticker} – MACD")
        ax.set_ylabel("MACD value")
        ax.legend()
        plt.show()

    def plot_rsi(self, period=14):
        """Plots RSI with overbought/oversold lines."""
        df = self.df
        ticker = self.ticker
        rsi_col = f"RSI_{period}"

        if rsi_col not in df.columns:
            self.calculate_rsi(period)

        fig, ax = plt.subplots(figsize=(12, 4))
        ax.plot(df.index, df[rsi_col], label=f"RSI {period}")
        ax.axhline(70, color="red", linestyle="--", label="Overbought (70)")
        ax.axhline(30, color="green", linestyle="--", label="Oversold (30)")

        ax.set_title(f"{ticker} – RSI({period})")
        ax.set_ylabel("RSI value")
        ax.legend()
        plt.show()