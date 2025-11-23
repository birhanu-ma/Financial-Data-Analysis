import matplotlib.pyplot as plt

def plotPriceAndSMA(df, ticker):
    """
    Plots Price + SMA20 + SMA50 (and Bollinger Bands if available).
    """

    fig, ax = plt.subplots(figsize=(14, 6))

    # ---- Price ----
    ax.plot(df.index, df["Close"], label="Price", color="black")

    # ---- SMA 20 ----
    if "SMA_20" in df.columns:
        ax.plot(df.index, df["SMA_20"], label="SMA 20", linestyle="--")

    # ---- SMA 50 ----
    if "SMA_50" in df.columns:
        ax.plot(df.index, df["SMA_50"], label="SMA 50", linestyle="-.")

    # ---- Labels ----
    ax.set_title(f"{ticker} – Price & Moving Averages")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price ($)")
    ax.legend()

    plt.show()
