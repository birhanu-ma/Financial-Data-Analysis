import matplotlib.pyplot as plt

def plotPrice(df, ticker):
    """
    Plots price and volume charts for a given ticker:
    - Close Price
    - Volume
    - High
    - Low
    - Open
    """

    # Close Price
    df["Close"].plot(title=f"{ticker} Close Price")
    plt.ylabel("Price ($)")
    plt.show()

    # Volume
    df["Volume"].plot(title=f"{ticker} Daily Volume")
    plt.ylabel("Shares Traded")
    plt.show()

    # High Price
    df["High"].plot(title=f"{ticker} High Price")
    plt.ylabel("Price ($)")
    plt.show()

    # Low Price
    df["Low"].plot(title=f"{ticker} Low Price")
    plt.ylabel("Price ($)")
    plt.show()

    # Open Price
    df["Open"].plot(title=f"{ticker} Open Price")
    plt.ylabel("Price ($)")
    plt.show()
