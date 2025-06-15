import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Inventory Tracker API"}