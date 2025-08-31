import fastapi
import uvicorn
import os
import json
from documents import documents

from fastapi.responses import FileResponse

import database
from pydantic import BaseModel

app = fastapi.FastAPI()
app.include_router(documents)

forms = {}
lenght_forms = 0

class UserFormInfo(BaseModel):
    id: str
    name: str
    phone: str
    tour: str


@app.get("/")
def startMes():
    return {"Status": "good"}


@app.post("/newUserDt")
def newUserDt(info: UserFormInfo):
    print(info)
    forms[info.id] = info
    return {"Status": "good"}


@app.get("/get_user_for_tg/{id}")
def get_user(id: str):
    return forms[id]


@app.get("/get_white_id")
def get_user():
    lenght_forms = lenght_forms + 1
    return str(lenght_forms)


@app.get("/reviews/{tour}")
def get_all_reviews(tour: str):
    try:
        with open(f"reviews.json", "r", encoding='utf-8') as f:
            if tour == "all":
                data = json.load(f)
                return data
    except FileNotFoundError:
        raise fastapi.HTTPException(status_code=404, detail="Review data not found")
    except json.JSONDecodeError:
        raise fastapi.HTTPException(status_code=500, detail="Error reading review data")


@app.get("/tours/{tour_id}")
def get_tour_info(tour_id: str):
    try:
        with open(f"programs/{tour_id}.json", "r", encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise fastapi.HTTPException(status_code=404, detail="Tour data not found")
    except json.JSONDecodeError:
        raise fastapi.HTTPException(status_code=500, detail="Error reading tour data")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)