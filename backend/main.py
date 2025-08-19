import fastapi
import uvicorn
import os
import json

app = fastapi.FastAPI()

@app.get("/")
def startMes():
    return {"Hello": "world"}


@app.get("/tours/{tour_id}")
def get_tour_info(tour_id: str):
    try:
        with open(f"{tour_id}.json", "r", encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise fastapi.HTTPException(status_code=404, detail="Tour data not found")
    except json.JSONDecodeError:
        raise fastapi.HTTPException(status_code=500, detail="Error reading tour data")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)