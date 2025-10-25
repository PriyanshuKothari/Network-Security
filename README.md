# 🚀 Network Security ML Project

---

## 🔍 Project Overview
This project demonstrates an **end-to-end Machine Learning lifecycle** for **network security**, focusing on **phishing detection**. It integrates **MLOps best practices**, including:

- Data ingestion & ETL pipelines  
- Model training & evaluation  
- Experiment tracking with **MLflow**  
- Deployment-ready Flask API  
- Data validation & quality checks  

This project reflects practical experience in **real-world AI/ML pipelines**.

---

## Key Features
- **Data Management**: ETL pipelines for processing network security datasets.
- **Model Training**: Trained multiple ML models including classification models to detect phishing attempts.
- **Experiment Tracking**: Integrated MLflow for experiment logging and model versioning.
- **Deployment**: Prediction API with Flask for real-time inference.
- **Output Management**: Structured storage of predictions and model artifacts.
- **Data Validation**: Schema enforcement and data quality checks.
---

## 📊 Architecture Diagram
```bash
+-------------------+
| Network Data |
| (CSV/Raw) |
+---------+---------+
|
v
+-------------------+
| ETL Pipeline |
| (Cleaning, Feature|
| Engineering) |
+---------+---------+
|
v
+-------------------+
| Model Training |
| (Classification) |
+---------+---------+
|
v
+-------------------+
| MLflow Tracking |
| (Experiments, |
| Model Versioning) |
+---------+---------+
|
v
+-------------------+
| Flask API |
| (Real-time |
| Predictions) |
+-------------------+

```
---
## 📂 Folder Structure
```bash
Network Security
    ├── Network_Data/ # Raw and processed datasets
    ├── final_models/ # Trained ML models
    ├── mlruns/ # MLflow experiment logs
    ├── networksecurity/ # Core ML pipeline scripts
    ├── prediction_output/ # Model prediction results
    ├── valid_data/ # Validated datasets
    ├── templates/ # Web interface templates
    ├── app.py # Flask API for real-time inference
    ├── main.py # Main pipeline execution script
    ├── push_data.py # Script to push data to database
    ├── requirements.txt # Python dependencies
    ├── Dockerfile # Containerization for deployment
    └── README.md
```
---
| Folder/File          | Description |
|---------------------|-------------|
| `Network_Data/`      | Raw and processed datasets |
| `final_models/`      | Trained ML models |
| `mlruns/`            | MLflow experiment logs |
| `networksecurity/`   | Core ML pipeline scripts |
| `prediction_output/` | Model predictions |
| `valid_data/`        | Validated datasets |
| `templates/`         | Flask web interface templates |
| `app.py`             | Flask API for inference |
| `main.py`            | Main pipeline execution script |
| `push_data.py`       | Data ingestion script |
| `requirements.txt`   | Python dependencies |
| `Dockerfile`         | Containerization |

--- 
## 💻 Technologies Used
- **Python** (Pandas, NumPy, Scikit-learn)  
- **MLflow** for experiment tracking and model versioning  
- **Flask** for deployment API  
- **Docker** for containerization  

--- 

## ⚡ Features
- End-to-end ML lifecycle for network security  
- Experiment tracking and model versioning with MLflow  
- Real-time prediction API using Flask  
- ETL pipelines for clean, structured data  
- Data validation and schema enforcement  
---


---
## 🛠️ How to Run Locally
1. Clone this repository:
```bash
git clone git clone https://github.com/PriyanshuKothari/Network-Security.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the pipeline:
```bash
python main.py
```
4. Start Flask API:
```bash
python app.py
```
---
## 🏆 Learning Outcomes

- Full MLOps lifecycle experience.

- Hands-on data engineering and ETL pipeline development.

- Practical experience with MLflow and model versioning.

- Real-world application in network security analytics.
---

## 👨‍💻 About Me

I’m currently a final year B.Tech student, learning AI/ML and MLOps.
I’m open to opportunities, feedback, and collaborations 🚀

### 📌 Connect with me:

- [LinkedIn](https://www.linkedin.com/in/priyanshu-kothari-1044b32bb/)

- [GitHub](https://github.com/PriyanshuKothari)
