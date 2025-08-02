# 🧠 Salary Prediction using Ensemble Machine Learning

This project builds a machine learning model that predicts employee salaries based on job-related features such as education, experience, location, and more. The final model is an ensemble of Random Forest and Gradient Boosting Regressors, combined using a Voting Regressor.

---

## 🔗 Live Demo

👉 [Click here to try the live app](https://ewpjwluslavixm5qunsjgb.streamlit.app/)

---

## 📁 Dataset

The dataset (`salary_train.csv`) contains anonymized employee information with the following features:

- `education_level`
- `age`
- `years_experience`
- `certifications`
- `job_title`
- `industry`
- `location`
- `company_size`
- `working_hours`
- `salary` (target)

---

## ⚙️ Data Preprocessing

- Removed unnecessary columns: `ID`, `crucial_code`
- Handled missing values:
  - Mode imputation for categorical features
  - Median/mean imputation for numerical features
- Encoded categorical columns using `LabelEncoder`
- Scaled numerical columns (`age`, `working_hours`) using `StandardScaler`

---

## 🧪 Model

An **ensemble model** is trained using:

- **Random Forest Regressor**
- **Gradient Boosting Regressor**

These are combined using a **Voting Regressor** to enhance predictive performance.

---

## 🧾 Metrics

Model performance on the test set:

- **R² Score**: `{{ your R2 score here }}`
- **Mean Absolute Error**: `{{ your MAE here }}`

---

## 📦 Pickled Files

These files are saved for deployment:

| File | Description |
|------|-------------|
| `regressor.pkl` | Final trained Voting Regressor model |
| `label_encode.pkl` | LabelEncoder used for categorical encoding |
| `standard_scaler.pkl` | Scaler for standardizing numeric columns |
| `data.pkl` | Dictionary of original feature values for UI dropdowns |

---

## 🖥 Streamlit App (Optional)

The model is deployed as a web app using [Streamlit](https://streamlit.io/). Users can input job-related features and instantly get salary predictions.

➡️ [Try the app here](https://ewpjwluslavixm5qunsjgb.streamlit.app/)

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/salary-prediction-ml.git
   cd salary-prediction-ml
