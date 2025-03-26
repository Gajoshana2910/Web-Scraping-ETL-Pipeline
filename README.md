<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 13bec14 (Initial commit - Web Scraping ETL Pipeline)
# 🛠️ Web Scraping ETL Pipeline  

This project is a simple **ETL (Extract, Transform, Load) pipeline** that scrapes quotes from [Quotes to Scrape](https://quotes.toscrape.com), cleans the data, and saves it to a CSV file.  

---

## 📌 Features  
✅ **Extracts** quotes and author names using web scraping (**BeautifulSoup**).  
✅ **Cleans and standardizes** data using **Pandas**.  
✅ **Saves** transformed data as a **CSV file** for further use.  

---

## 🏗️ Project Structure  

```
📂 Web Scraping ETL Pipeline
│── 📂 scripts
│   ├── extract.py        # Extracts data from the website
│   ├── transform.py      # Cleans and standardizes the data
│   ├── load.py           # Saves the data to a CSV file
│── 📄 main.py            # Runs the complete ETL process
│── 📄 requirements.txt   # List of dependencies
│── 📄 README.md          # Project documentation
```
## 🚀 Installation & Setup
1️⃣ Clone the Repository
```
git clone https://github.com/Gajoshana2910/Web-Scraping-ETL-Pipeline.git
cd Web-Scraping-ETL-Pipeline
```
2️⃣ Set Up a Virtual Environment (Optional, Recommended)
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
🔄 Running the ETL Pipeline
Run the main script to execute the entire ETL process:
```
python main.py
```
## 📌 Sample Output
```
[INFO] Starting ETL process...
[INFO] Extraction successful!
[INFO] Transformation successful!
[INFO] Data saved to data/scraped_data.csv
[INFO] ETL process completed successfully! 🚀
```
## 📜 Code Overview

1️⃣ Extract Data (scripts/extract.py)

- Scrapes quotes and authors from the website.
- Handles missing author names.
- Stores extracted data in a Pandas DataFrame.

2️⃣ Transform Data (scripts/transform.py)

- Cleans special characters from quotes.
- Capitalizes author names.

3️⃣ Load Data (scripts/load.py)

- Saves the cleaned data as data/scraped_data.csv.

## 📂 Output File

After running the ETL pipeline, the cleaned data will be saved as:
```
📂 data
   ├── scraped_data.csv
```

## 📦 Dependencies
This project requires the following Python libraries:
```
beautifulsoup4
pandas
requests
```
You can install them using:
```
pip install -r requirements.txt
```

## 🛠️ Next Steps / Improvements
```
✅ Add Airflow/Docker for automation.
✅ Store data in a database (PostgreSQL, Snowflake, etc.) instead of CSV.
✅ Scrape multiple pages instead of just the first one.
```
## 📜 License

This project is licensed under the MIT License 
👉 see the [LICENSE](https://github.com/Gajoshana2910/Web-Scraping-ETL-Pipeline/blob/main/LICENSE) file for details.  

## 👨‍💻 Developed by

👉 [Gajalakshmi A K](https://github.com/Gajoshana2910)

<<<<<<< HEAD
=======
=======
 
>>>>>>> 081b8f6 (Initial commit - Web Scraping ETL Pipeline)
>>>>>>> 13bec14 (Initial commit - Web Scraping ETL Pipeline)
