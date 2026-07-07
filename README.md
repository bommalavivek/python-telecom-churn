#  Telecom Customer Churn Analysis

##  Project Overview
This project focuses on analyzing customer churn behavior in the telecom industry using Python.  
Customer churn refers to customers discontinuing a service, which directly impacts revenue and business sustainability.

The objective of this project is to identify key factors that influence customer churn and generate actionable business insights.



##  Business Problem
Telecom companies face significant losses when customers leave their services.  
Understanding **why customers churn** helps organizations:
- Improve customer retention
- Optimize pricing strategies
- Design better contract plans



##  Dataset Description
The dataset contains customer-level information, including:
- Demographics
- Service usage
- Billing details
- Contract information
- Churn status (target variable)

**Target Variable:**
- `Churn`  
  - Yes → Customer left  
  - No → Customer stayed  

---

##  Tools & Technologies Used
- **Python**
- **Pandas & NumPy** – data manipulation
- **Matplotlib & Seaborn** – data visualization
- **Jupyter Notebook** – exploratory analysis
- **Git & GitHub** – version control

---

##  Project Structure
python-telecom-churn/
│
├── data/
│ ├── raw/
│ │ └── telecom_churn.csv
│ └── processed/
│ └── telecom_churn_eda_ready.csv
│
├── src/
│ ├── data_cleaning.py
│ ├── feature_engineering.py
│ ├── notebooks/
│ │ └── 01_eda.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore




##  Exploratory Data Analysis (EDA)
The analysis follows a structured EDA approach:

### 1. Data Understanding
- Dataset shape and structure
- Data types and missing values
- Identification of numerical and categorical features

### 2. Churn Distribution
- Analysis of churn vs non-churn customers
- Identification of class imbalance

### 3. Monthly Charges vs Churn
- Customers with higher monthly charges tend to churn more
- Indicates pricing sensitivity

### 4. Tenure vs Churn
- New customers are significantly more likely to churn
- Customer retention improves with longer tenure

### 5. Contract Type vs Churn
- Month-to-month contracts have the highest churn rate
- Long-term contracts reduce churn risk

### 6. Correlation Analysis
- Tenure shows strong negative correlation with churn
- Monthly charges show a positive relationship with churn



##  Key Business Insights
- High churn occurs among **new customers**
- **Month-to-month contracts** are high risk
- Customers with **higher monthly charges** churn more
- Long-term engagement significantly reduces churn


##  Business Recommendations
- Improve onboarding experience for new customers
- Encourage long-term contracts through incentives
- Introduce targeted discounts for high-risk customers
- Monitor pricing sensitivity among premium users



##  Output
- Exported EDA-ready dataset for SQL & Power BI analysis:
  - `data/processed/telecom_churn_eda_ready.csv`



##  Next Steps
- SQL-based churn analysis
- Power BI dashboard for executive reporting
- Predictive churn modeling (Machine Learning)

