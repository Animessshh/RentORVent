# 🏠 RentORVent (https://rentorvent.streamlit.app/)

### Predict. Compare. Decide.

RentORVent is an AI-powered rental fairness and pricing analyzer that helps both tenants and property owners make informed rental decisions using Machine Learning.

The system predicts property rental prices based on key housing features and provides:

* 🔍 **Rent Fairness Checker** for tenants
* 🏢 **Rental Price Analyzer** for property owners
* 📈 Machine Learning based rent prediction
* ⚖️ Fairness evaluation of quoted rents
* 💡 Data-driven rental recommendations

---

# 🚀 Features

## 🔍 Rent Fairness Checker

Designed for customers looking for rental properties.

Users can:

1. Select property details
2. View the ML-predicted fair rent
3. Enter the quoted rent provided by the owner
4. Receive an affordability and fairness assessment

Possible outcomes:

* 🟢 Fair Price
* 🔵 Good Deal
* ⭐ Excellent Deal
* 🟡 Slightly Overpriced
* 🔴 Significantly Overpriced

---

## 🏢 Rental Price Analyzer

Designed for landlords and property owners.

Users can:

1. Enter property details
2. Obtain a recommended rental price
3. View a suggested listing range
4. Analyze their property's market positioning

---

# 🧠 Machine Learning Workflow

The project follows a complete machine learning pipeline:

```text
Raw Dataset
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Encoding & Scaling
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Deployment using Streamlit
```

---

# 📊 Dataset Overview

The dataset contains rental listings from major Indian cities.

### Features

| Feature       | Description                    |
| ------------- | ------------------------------ |
| locality      | Property locality              |
| city          | City name                      |
| area          | Area in square feet            |
| beds          | Number of bedrooms             |
| bathrooms     | Number of bathrooms            |
| balconies     | Number of balconies            |
| furnishing    | Furnishing status              |
| property_type | Flat / House / Villa           |
| rent          | Monthly rent (Target Variable) |

### Dataset Statistics

* Total Records: **7,691**
* Cities: **5**
* Localities: **51**
* Property Types: **3**
* Furnishing Categories: **3**

---

# 📁 Project Structure

```text
RentORVent/
│
├── Rent_cleaned_data.csv
├── Rent_predictor.pkl
├── mockapp.py
├── prt1.ipynb
├── prt2.ipynb
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📘 Notebook Descriptions

## 📓 prt1.ipynb

### Data Cleaning & Feature Engineering

This notebook focuses on preparing the raw rental dataset for machine learning.

### Tasks Performed

#### Data Exploration

* Dataset inspection
* Missing value analysis
* Duplicate value detection
* Feature distribution analysis

#### Feature Engineering

Extracted **property_type** from the `house_type` column using Regular Expressions.

Example:

```text
2 BHK Flat for Rent
          ↓
Flat
```

#### Feature Selection

Removed redundant features:

* house_type
* area_rate

These columns either duplicated existing information or introduced potential target leakage.

#### Locality Optimization

Reduced locality cardinality to improve model performance and deployment usability.

#### Output

Generated the final cleaned dataset:

```text
Rent_cleaned_data.csv
```

---

## 📓 prt2.ipynb

### Model Development & Training

This notebook contains the complete machine learning workflow.

### Steps Performed

#### Train-Test Split

```python
train_test_split(
    test_size=0.2,
    random_state=42
)
```

---

#### Correlation Analysis

Investigated relationships among numerical variables:

* area
* beds
* bathrooms
* balconies

Used heatmaps to identify multicollinearity.

---

#### Data Preprocessing

Implemented:

### Numerical Features

* StandardScaler

### Categorical Features

* OneHotEncoder

using:

```python
ColumnTransformer
```

---

### Models Evaluated

#### Linear Regression

Baseline model

---

#### Lasso Regression

Feature selection through L1 regularization

---

#### LassoCV

Automatic alpha selection using cross-validation

---

#### Ridge Regression

L2 regularization

---

#### RidgeCV

Cross-validated ridge model

---

#### Polynomial Regression

Polynomial feature expansion with degree = 2

This significantly improved performance over standard linear models.

---

### Final Model

A unified deployment-ready pipeline:

```python
full_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('poly', PolynomialFeatures(
        degree=2,
        include_bias=False
    )),
    ('lr', LinearRegression())
])
```

---

### Model Serialization

Saved using Pickle:

```python
pickle.dump(
    full_pipeline,
    open('Rent_predictor.pkl', 'wb')
)
```

This enables direct deployment without retraining.

---

# 💻 mockapp.py

### Streamlit Web Application

The frontend interface for RentORVent.

### Functionalities

#### Landing Page

Users choose between:

* Customer Mode
* Property Owner Mode

---

#### Customer Mode

Allows users to:

* Predict fair rental price
* Enter quoted rent
* Perform fairness analysis

---

#### Property Owner Mode

Allows users to:

* Estimate market rent
* View recommended listing range
* Analyze property positioning

---

### Technologies Used

* Streamlit
* Pandas
* Scikit-Learn
* Pickle

---

# 🛠️ Tech Stack

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn

### Deployment

* Streamlit

---

# 📈 Model Performance

Final deployed model:

### Polynomial Regression Pipeline

Performance metrics:

```text
R² Score ≈ 0.69
MAE ≈ ₹22,500
```

(Values may vary slightly depending on train-test split.)

---

# 🎯 Future Improvements

* SHAP Explainability
* Interactive Rent Comparison Dashboard
* Rental Trend Analysis
* Geographic Visualization
* Property Recommendation Engine
* Advanced Ensemble Models (Random Forest, XGBoost)

---

# 👨‍💻 Author

**Animesh Sharma**

Computer Science Engineering Student
Machine Learning | Data Science | AI Enthusiast
