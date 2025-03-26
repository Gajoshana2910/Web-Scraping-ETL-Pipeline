<<<<<<< HEAD
# Import ETL functions from scripts
from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load

# 🏁 Run the ETL Process
print("[INFO] Starting ETL process...")

# 1️⃣ Extract: Scrape data from the website
data = extract()
if data is not None:
    print("[INFO] Extraction successful!")
else:
    print("[ERROR] Extraction failed. Exiting...")
    exit()

# 2️⃣ Transform: Clean and standardize the data
cleaned_data = transform(data)
if cleaned_data is not None:
    print("[INFO] Transformation successful!")
else:
    print("[ERROR] Transformation failed. Exiting...")
    exit()

# 3️⃣ Load: Save the cleaned data to a CSV file
load(cleaned_data)

print("[INFO] ETL process completed successfully! 🚀")
=======
# Import ETL functions from scripts
from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load

# 🏁 Run the ETL Process
print("[INFO] Starting ETL process...")

# 1️⃣ Extract: Scrape data from the website
data = extract()
if data is not None:
    print("[INFO] Extraction successful!")
else:
    print("[ERROR] Extraction failed. Exiting...")
    exit()

# 2️⃣ Transform: Clean and standardize the data
cleaned_data = transform(data)
if cleaned_data is not None:
    print("[INFO] Transformation successful!")
else:
    print("[ERROR] Transformation failed. Exiting...")
    exit()

# 3️⃣ Load: Save the cleaned data to a CSV file
load(cleaned_data)

print("[INFO] ETL process completed successfully! 🚀")
>>>>>>> 081b8f6 (Initial commit - Web Scraping ETL Pipeline)
