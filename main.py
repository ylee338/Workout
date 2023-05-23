# Import required modules
from nutritionix import Nutritionix
from sheet import Sheety

# Ask the user for the exercises they did
user_query = input("Which exercises have you performed today: ")

# Create the Nutritionix Object & post the data
nx_object = Nutritionix(query=user_query, gender="male", weight_kg=71, height_cm=179, age=23)
nx_post_data = nx_object.post_response()

# loop through each exercise
for key in range(0, len(nx_post_data.json()["exercises"])):
    # Create Sheety object and post
    sheety_object = Sheety(exercise=nx_post_data.json()["exercises"][key]["name"].title(),
                           duration=nx_post_data.json()["exercises"][key]["duration_min"],
                           calories=nx_post_data.json()["exercises"][key]["nf_calories"])
    sheety_post_response = sheety_object.post_response()
    print(sheety_post_response.text)