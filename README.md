# Car Price Predictor 🚗💰

A Machine Learning–based web application that predicts the resale price of used cars based on features such as manufacturing year, kilometers driven, fuel type, and brand.

---

## 🚀 Project Overview

Buying or selling a used car can be confusing when it comes to deciding the right price.  
This project simplifies that process by using a trained **Linear Regression model** to provide instant and data-driven price predictions through a web interface.

---

## 🖼️ Demo Screenshot

![Car Price Predictor Demo](https://github.com/Bittu169/car-price-predictor/blob/b300950626cb52d37fd473af936132456c87efae/Screenshot%202026-02-15%20200637.png?raw=true)

---

## ✨ Features

- ✅ User-friendly web interface
- ✅ Real-time car price prediction
- ✅ Supports multiple car brands
- ✅ ML model trained on real-world car data
- ✅ Deployed using Flask & Gunicorn

---

## 🛠️ Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript

**Backend**
- Flask
- Gunicorn

**Machine Learning**
- Python
- Scikit-learn
- Pandas
- NumPy

**Dataset**
- Kaggle Used Car Dataset (sourced from :contentReference[oaicite:0]{index=0})

---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Bittu169/car-price-predictor.git
cd car-price-predictor
```
### 2️⃣ Create a virtual environment
```bash
python -m venv venv
Activate it:

Windows

venv\Scripts\activate
Linux / macOS


source venv/bin/activate
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the application
```bash
python app.py
Open in browser:

http://127.0.0.1:5000
```
### 📊 Model Input Features
The prediction model considers:

Company – Car manufacturer

Car Model – Specific model name

Year – Manufacturing year

Kms Driven – Total kilometers driven

Fuel Type – Petrol / Diesel / CNG

### 🌐 Deployment
This project is deployed on Render using:

gunicorn app:app

Python 3.10

Flask production server

Live URL:

https://car-price-predictor-7yra.onrender.com
### 🤝 Contributing
Contributions are welcome!
If you find a bug or want to improve the project:

Fork the repository

Create a new branch

Commit your changes

Open a Pull Request on GitHub

### 📜 License
This project is licensed under the MIT License.


---

## ✅ What to do next

1. Replace your current `README.md` with this one  
2. Commit and push:
```bash
git add README.md
git commit -m "Fix README formatting and documentation"
git push
```
