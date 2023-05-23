import requests


APP_ID = "debad296"
API_KEY = "4a1e979e8258bf9dc351a839964f8068"

GENDER = "Male"
WEIGHT_KG = "71"
HEIGHT_CM = "179"
AGE = "23"

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("What exercise did you do?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {"query": exercise_input,
              "gender": GENDER,
              "weight_kg": WEIGHT_KG,
              "height_cm": HEIGHT_CM,
              "age": AGE
}

response = requests.post(endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


