import pickle
from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

model = pickle.load(open("LinearRegressionModel.pkl", "rb"))
car = pd.read_csv("Cleanned_Car.csv")

@app.route("/")
def index():
    companies = sorted(car["company"].unique())
    years = sorted(car["year"].unique(), reverse=True)
    fuel_type = car["fuel_type"].unique()

    company_to_models = {}
    for company in companies:
        models = sorted(car[car["company"] == company]["name"].unique())
        company_to_models[company] = models

    return render_template(
        "index.html",
        companies=companies,
        years=years,
        fuel_type=fuel_type,
        company_to_models=company_to_models
    )

@app.route("/predict", methods=["POST"])
def predict():
    company = request.form.get("company")
    car_model = request.form.get("car_model")
    year = int(request.form.get("year"))
    fuel_type = request.form.get("fuel_type")
    kilo_driven = int(request.form.get("kilo_driven"))

    prediction = model.predict(
        pd.DataFrame(
            [[car_model, company, year, kilo_driven, fuel_type]],
            columns=["name", "company", "year", "kms_driven", "fuel_type"]
        )
    )

    return str(np.round(prediction[0], 2))

if __name__ == "__main__":
    app.run()
