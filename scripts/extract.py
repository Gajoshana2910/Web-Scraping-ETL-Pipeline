import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract():
    """Extract data from a website (e.g., quotes.toscrape.com)"""
    
    url = "https://quotes.toscrape.com/"  # Website URL for scraping quotes
    response = requests.get(url)  # Sending a request to fetch the webpage

    if response.status_code != 200:  # Checking if the request was successful
        print("[ERROR] Failed to fetch data")
        return None

    soup = BeautifulSoup(response.text, "html.parser")  # Parsing the webpage content
    quotes_data = []  # List to store extracted quotes and authors

    # Loop through each quote block (div with class="quote")
    for quote_block in soup.find_all("div", class_="quote"):
        
        # Extract the quote text (inside <span class="text">)
        quote_text = quote_block.find("span", class_="text").text.strip()

        # Extract the author name (inside <small class="author">)
        author_tag = quote_block.find("small", class_="author")  # Correct selection
        author = author_tag.text.strip() if author_tag else "Unknown"  # Handle missing author

        # Store the extracted data as a dictionary
        quotes_data.append({"quote": quote_text, "author": author})

    # Convert list of dictionaries into a Pandas DataFrame
    return pd.DataFrame(quotes_data)
