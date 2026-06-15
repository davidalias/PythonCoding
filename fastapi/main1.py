from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class AvailableCuisines(str, Enum):
   indian = "indian"
   american = "american"
   italian = "italian" 

food_items = {
    "indian": ["Samosa", "Dosa"],
    "american" : ['hot dog', "apple pie"],
    "italian": ['ravioli', 'pizza']
}

@app.get("/get_items/{cuisine}")
def get_items(cuisine:AvailableCuisines):
    return food_items.get(cuisine)