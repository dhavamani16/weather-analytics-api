#  Weather Analytics API

A simple backend API built using **FastAPI** to load, store, and analyze weather data.  
This project demonstrates how to build REST APIs, work with databases, and process real-world data.

---

##  Features

- FastAPI-based REST API  
- Load weather data from CSV file  
- Store data in SQLite database  
- Fetch weather data by city  
- Basic analytics support  
- Easy to understand and extend  

---

##  Tech Stack

- **Python**
- **FastAPI**
- **Uvicorn**
- **SQLite**
- **Pandas**

---

## 📁 Project Structure
```text
weather-analytics-api/
│── api/                # API routes
│── data/               # Dataset (weather.csv)
│── load_data.py        # Load CSV to DB
│── main.py             # Main API file
│── weather.db          # Database
│── README.md
