# Payment Analytics

A portfolio project for analyzing payment transaction data using SQL and Python.

## Overview

This project demonstrates a typical payment analytics workflow using synthetic transaction data.

The analysis includes:

* Total payment volume
* Commission revenue
* Active users
* Average transaction amount
* Transaction success rate
* Category-level analysis
* Daily transaction dynamics
* Top users by transaction volume

## Dataset

The project uses a synthetic dataset:

`transactions.csv`

Main fields:

* `transaction_id`
* `user_id`
* `transaction_date`
* `category`
* `amount`
* `commission`
* `status`

All data in this repository is synthetic and created specifically for demonstration purposes.

## SQL Analysis

The file `analysis.sql` contains SQL queries for:

* Total transaction volume
* Total commission revenue
* Transaction count by status
* Active users
* Average transaction amount
* Category analysis
* Daily transaction dynamics
* Top users by payment volume
* Transaction success rate

## Python Analysis

The file `payment_analysis.py` performs the same type of analytical processing using Python and pandas.

The script:

* Loads transaction data
* Filters successful transactions
* Calculates key KPIs
* Builds category-level analysis
* Analyzes daily transaction dynamics
* Identifies top users by payment volume
* Saves analytical results to Excel

## Output

The Python script generates:

`payment_analysis_results.xlsx`

The workbook contains four sheets:

### KPIs

Main business metrics:

* Total Payment Volume
* Total Commission Revenue
* Active Users
* Average Transaction Amount
* Success Rate

### Categories

Analysis by transaction category:

* Transaction count
* Total amount
* Total commission
* Average transaction amount

### Daily Dynamics

Daily transaction performance:

* Transaction count
* Daily payment volume
* Daily commission

### Top Users

User-level analysis based on transaction volume.

## Tech Stack

* SQL
* Python
* pandas
* openpyxl
* Microsoft Excel

## Project Structure

* `transactions.csv` — synthetic transaction dataset
* `analysis.sql` — SQL analytical queries
* `payment_analysis.py` — Python analytical script
* `payment_analysis_results.xlsx` — generated analytical report
* `requirements.txt` — Python dependencies
* `README.md` — project documentation

## How to Run

### 1. Install dependencies

`pip install -r requirements.txt`

### 2. Make sure the transaction dataset is in the project folder

`transactions.csv`

### 3. Run the Python analysis

`python payment_analysis.py`

### 4. Check the generated report

`payment_analysis_results.xlsx`

## Skills Demonstrated

* SQL analytics
* Python data analysis
* Payment analytics
* Transaction analysis
* KPI calculation
* Data aggregation
* Product analytics
* Financial analytics
* Excel reporting

## Data Privacy

All transaction data used in this repository is synthetic.

The repository does not contain confidential, customer, production, or employer data.

## Future Improvements

* Add monthly and weekly metrics
* Add MAU / DAU analysis
* Add retention metrics
* Add transaction segmentation
* Add automated visualizations
* Add anomaly detection
* Add Power BI dashboard
