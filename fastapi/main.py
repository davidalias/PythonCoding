from fastapi import FastAPI

app = FastAPI()

food_items = {
    "indian": ["Samosa", "Dosa"],
    "american" : ['hot dog', "apple pie"],
    "italian": ['ravioli', 'pizza']
}

@app.get("/get_items/{cuisine}")
def get_items(cuisine):
    return food_items.get(cuisine)