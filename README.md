# 🚗 AlphaCare Risk Analytics: Insurance Risk & Premium Modeling (B5W3)

This project is a data analytics challenge thatfocused on analyzing car insurance data to identify low-risk client segments and optimize premiums.

## 📁 Project Structure

```
├── .github/
├── data/
│ ├── raw/
| | └── .gitignore
│ │ └── MachineLearningRating_v3.csv
    └── MachineLearningRating_v3.csv.csv
│ └── processed/
├── notebooks/
│ └── 01_data_understanding.ipynb
├──scripts/
├──src/
├──tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## 📌 Tasks Overview

### ✅ Task 1: Data Understanding & EDA

- Data structure inspection
- Missing values analysis
- Univariate & bivariate plots
- Loss Ratio computation
- Outlier detection
- visualizations

### ✅ Task 2: Data Understanding & EDA

- Installed and initialized [DVC]
- Created local remote storage: `~/dvc-storage/insurance-risk-project`
- Added raw data to version control using:
  ```bash
  dvc add data/raw/MachineLearningRating_v3.csv
  ```

* Committed .dvc file to Git and pushed data to local storage:

```bash
dvc push
```

## Reproducing the Project

```bash
dvc pull
```

## To run EDA notebooks:

```bash
jupyter notebook notebooks/01_data_understanding.ipynb
```

### 🔄 Future Tasks

- Task 2: Hypothesis Testing (A/B Tests on Province, Gender, etc.)
- Task 3: Predictive Modeling for Premiums
- Task 4: Reporting & Recommendations

## 📊 Key Questions

- What’s the overall Loss Ratio? How does it vary by gender, location, vehicle type?
- Are there temporal or geographic trends in claims/premiums?
- Which clients or vehicles contribute most to losses?

## 🛠 Tech Stack

- Python, Pandas, Seaborn, Matplotlib
- Jupyter Notebooks
- GitHub Actions (CI/CD)
- Git for version control

## 🧠 Learning Outcomes

- End-to-end insurance analytics using real-world data
- Solid grounding in EDA, hypothesis testing, and predictive modeling
- Writing modular, maintainable Python code

---

## 🔧 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/moablex/insurance-risk-analytics.git
cd insurance-risk-analytics

# 2. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```
