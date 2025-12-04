# 📊 Vendor Sales Analysis

This project focuses on analyzing vendor-wise sales performance using structured datasets and automated database ingestion. The goal is to generate insights that help understand vendor efficiency, sales trends, and inventory movement, supported by exploratory and performance analysis models.

---

## 🌐 View Interactive Dashboard
👉 [Click here to view the live Power BI dashboard](https://app.powerbi.com/view?r=eyJrIjoiMTQwNWNiNzEtMzllMC00MWQyLTgxZWUtYTY1MjEwZjczMTVjIiwidCI6IjljNjM5OGM0LTllMDktNDM2Ni1iOTNlLTEwNThiOGE5YTkyOCJ9).

---

## 📁 Project Structure

- **vendor_sales_summary.csv** <br> Final aggregated vendor-wise sales summary data used for analysis.
- **Vendor Performance Analysis.ipynb** <br>Jupyter notebook that analyzes vendor performance across KPIs like revenue, quantity sold, and trend patterns.
- **Vendor Analysis Report.pdf** <br>Final analytical report summarizing insights, visualizations, and recommendations.
- **inventory.db** <br>SQLite database storing raw and processed transactional inventory data.
- **ingestion_db.py** <br> Script to ingest raw data files into the SQLite database (inventory.db).
- **ingestion_db.log** <br>Log file capturing the data ingestion process details and errors (if any).
- **get_vendor_summary.py** <br>Script to generate vendor summary output from database and export it to CSV.
- **get_vendor_summary.log** <br>Log file capturing execution details of get_vendor_summary.py.
- **Exploratory Data Analysis.ipynb** <br>Notebook performing initial exploratory data analysis, visualizations, and data cleaning.

---

## 🔧 Tech Stack

- Category	Tools / Technologies
- Language	Python
- Database	SQLite (inventory.db)
- Analysis	Pandas, NumPy
- Visualization	 Matplotlib, Seaborn
- Notebooks	Jupyter Notebook

---

## 🚀 Workflow Overview

- **Data Collection** <br>
Raw vendor-related datasets stored in the data/ folder.

- **Database Ingestion** <br>
ingestion_db.py reads raw CSV/text data and loads it into inventory.db.
Execution logs maintained in ingestion_db.log.

- **Summary Generation** <br>
get_vendor_summary.py extracts and aggregates vendor-level metrics.
Output saved as vendor_sales_summary.csv & logs stored in get_vendor_summary.log.

- **Exploratory Data Analysis** <br>
Conducted using Exploratory Data Analysis.ipynb.

- **Vendor Performance Deep Dive** <br>
Detailed performance comparisons and insights extracted using Vendor Performance Analysis.ipynb.

- **Final Report** <br>
Findings compiled into Vendor Analysis Report.pdf.

---

## 📌 Key Insights

- Identification of top-performing vendors by revenue and sales volume.

- Detection of declining or inconsistent vendor performance.

- Sales seasonality trends & vendor contribution percentages.

- Actionable recommendations for vendor selection and stock strategy.

---

## ▶️ How to Run

- Step 1: Run ingestion script
python ingestion_db.py

- Step 2: Generate vendor sales summary
python get_vendor_summary.py

- The CSV summary will be saved as:
vendor_sales_summary.csv

---

## 👩‍💻 Author
**Namrata Shitole**  
🌐 [LinkedIn Profile](https://www.linkedin.com/in/namrata-shitole-2a800536)