import matplotlib.pyplot as plt
import talib

def plotRSI(df, ticker, period=14):
    """
    Calculates and plots RSI for a given ticker.
    Automatically computes RSI if missing.
    """

    # ---- Ensure 'Close' exists ----
    if "Close" not in df.columns:
        raise ValueError("DataFrame must contain 'Close' column to calculate RSI")

    # ---- Convert Close to 1D numpy array ----
    close_prices = df["Close"].to_numpy().ravel()  # <-- ensures 1D array

    # ---- Calculate RSI ----
    rsi_col = f"RSI_{period}"
    df[rsi_col] = talib.RSI(close_prices, timeperiod=period)

    # ---- Plot ----
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df.index, df[rsi_col], label=f"RSI {period}")
    ax.axhline(70, color="red", linestyle="--", label="Overbought (70)")
    ax.axhline(30, color="green", linestyle="--", label="Oversold (30)")

    ax.set_title(f"{ticker} – RSI({period})")
    ax.set_ylabel("RSI value")
    ax.legend()
    plt.show()
