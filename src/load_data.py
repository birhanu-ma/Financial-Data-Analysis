import yfinance as yf

def loadData(ticker, start_date="2009-01-01", end_date="2023-12-29"):
    """
    Load historical stock data for a given ticker.
    
    Parameters:
        ticker (str)      : Stock ticker symbol (e.g. "GOOG")
        start_date (str)  : Start date in YYYY-MM-DD format
        end_date (str)    : End date in YYYY-MM-DD format
    
    Returns:
        pandas.DataFrame : Historical OHLCV data
    """
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    return df

# Example usage:
data = loadData("GOOG")
data.head()
