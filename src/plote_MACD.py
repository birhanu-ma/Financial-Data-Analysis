import matplotlib.pyplot as plt
import talib

def plotMACD(df, ticker):
    """
    Calculates and plots MACD, Signal line, and Histogram for a given ticker.
    Automatically computes MACD if missing.
    """

    # ---- Ensure 'Close' exists ----
    if "Close" not in df.columns:
        raise ValueError("DataFrame must contain 'Close' column to calculate MACD")

    # ---- Convert Close to 1D numpy array ----
    close_prices = df["Close"].to_numpy().ravel()

    # ---- Calculate MACD ----
    macd, signal, hist = talib.MACD(close_prices)
    df["MACD"] = macd
    df["MACD_signal"] = signal
    df["MACD_hist"] = hist

    # ---- Plot ----
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df.index, df["MACD"], label="MACD", color="blue")
    ax.plot(df.index, df["MACD_signal"], label="Signal", color="orange")
    ax.bar(df.index, df["MACD_hist"], label="Histogram", color="gray")

    ax.set_title(f"{ticker} – MACD")
    ax.set_ylabel("MACD value")
    ax.legend()
    plt.show()
