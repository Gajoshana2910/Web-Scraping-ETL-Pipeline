import pandas as pd  # Import pandas for handling data

def load(df, output_path="data/scraped_data.csv"):
    """Save extracted and transformed data to a CSV file."""

    # Check if the DataFrame is empty or None
    if df is None or df.empty:
        print("[ERROR] No data to load.")  # Print error message if no data is provided
        return  # Exit the function

    # Save the DataFrame to a CSV file (without the index column)
    df.to_csv(output_path, index=False)

    # Print confirmation message
    print(f"[INFO] Data saved to {output_path}")
