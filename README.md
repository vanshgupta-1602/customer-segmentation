# customer-segmentation
# Customer Segmentation Using K-Means Clustering

## 1. Project Overview

Customer Segmentation is a machine learning project that groups customers according to their annual income and spending scores using the K-Means clustering algorithm.

The project uses Python for data processing and machine learning, Matplotlib for visualization, and Streamlit to create an interactive dashboard. It helps businesses understand customer behavior and identify different customer groups for targeted marketing strategies.

## 2. Objectives

* Group customers into four segments using K-Means clustering.
* Analyze annual income and spending patterns.
* Visualize customer groups using scatter plots.
* Evaluate clustering quality using the Silhouette Score.
* Display results through an interactive web dashboard.

## 3. Technologies Used

* **Python** – Programming language
* **Pandas** – Data processing
* **Scikit-learn** – Machine learning and clustering
* **StandardScaler** – Feature scaling
* **Matplotlib** – Data visualization
* **Streamlit** – Interactive dashboard

## 4. Project Structure

```text
customersegmentation/
│
├── data/
│   └── customer.csv
│
├── venv/
│
├── app.py
├── clustering.py
└── README.md
```

## 5. Dataset Description

The dataset is stored in `data/customer.csv` and contains the following columns:

| Column        | Description                |
| ------------- | -------------------------- |
| CustomerID    | Unique customer identifier |
| Age           | Customer's age             |
| AnnualIncome  | Annual customer income     |
| SpendingScore | Customer spending score    |

The current dataset contains 20 sample customer records.

## 6. Installation and Setup

### Step 1: Install Python

Install Python from https://www.python.org/downloads/ if it is not already installed.

### Step 2: Open the Project Folder

Open the project folder in Visual Studio Code and open its terminal.

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it in Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Required Libraries

```bash
python -m pip install pandas scikit-learn matplotlib streamlit
```

## 7. How to Run the Project

### Run the Machine Learning Model

Execute:

```bash
python clustering.py
```

The program loads the dataset, applies K-Means clustering, assigns cluster IDs, and displays customer records with their cluster assignments.

### Run the Dashboard

Execute:

```bash
python -m streamlit run app.py
```

The dashboard opens in your web browser.

It displays:

* Customer records and assigned segments
* Cluster summary
* Silhouette Score
* Customer segmentation scatter plot

## 8. Working Methodology

1. **Data Loading:** Read customer records from the CSV file.
2. **Feature Selection:** Select AnnualIncome and SpendingScore.
3. **Feature Scaling:** StandardScaler standardizes the selected features.
4. **Clustering:** K-Means groups customers into four clusters.
5. **Evaluation:** Silhouette Score estimates how well-separated the clusters are.
6. **Visualization:** Matplotlib displays customer groups.
7. **Dashboard:** Streamlit presents the results in a user-friendly interface.

## 9. Customer Segments

The model creates four clusters. Their characteristics are determined from the resulting data:

* High-income customers with moderate spending
* Medium-income customers with higher spending
* Lower-income customers with higher spending
* High-income customers with lower spending

Cluster IDs are assigned by the algorithm and may change when the model or dataset changes. Segment names should be verified against the calculated cluster averages.

## 10. Expected Output

The project produces customer records with cluster assignments, average income and spending summaries for each cluster, a Silhouette Score, and a scatter plot showing the distribution of customers.

## 11. Applications

* Customer behavior analysis
* Targeted marketing campaigns
* Personalized offers and promotions
* Customer relationship management
* Business intelligence and analytics

## 12. Limitations

The project currently uses a small sample dataset of 20 customers. Results may not represent real-world customer behavior. The number of clusters is fixed at four, and the quality of segmentation depends on the dataset and selected features.

## 13. Future Enhancements

* Use a larger real-world customer dataset.
* Add interactive filters to the dashboard.
* Compare different numbers of clusters.
* Add more customer attributes.
* Improve the dashboard design and reporting features.

## 14. Conclusion

This project demonstrates how unsupervised machine learning can be used to identify customer groups based on income and spending behavior. By combining K-Means clustering, feature scaling, visualization, and a Streamlit dashboard, it provides a practical introduction to machine learning and customer analytics.

## 15. Author

**Name:** Vansh Gupta

**Project:** Customer Segmentation Using K-Means Clustering

**Domain:** Machine Learning and Data Analytics
