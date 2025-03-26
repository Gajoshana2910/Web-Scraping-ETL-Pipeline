import pandas as pd  # Import pandas for data transformation

def transform(df):
    """Clean and standardize the extracted data."""

    # Check if the DataFrame is empty or None
    if df is None or df.empty:
        print("[ERROR] No data to transform.")  # Print error message if no data
        return None  # Exit the function

    # Remove special characters (“ and ”) from the quotes
    df["quote"] = df["quote"].str.replace("“", "").str.replace("”", "", regex=True)

    # Standardize author names by capitalizing the first letter of each word
    df["author"] = df["author"].str.title()

    return df  # Return cleaned DataFrame
