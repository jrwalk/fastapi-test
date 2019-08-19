from fastapi import FastAPI
from starlette.responses import UJSONResponse

from app.schema import Input, Output, ScoreInput, ScoreOutput, ValidScores
from app.model import ModelWrapper


app = FastAPI()
model = ModelWrapper("/opt/fastapi-test/models/model.pkl")

@app.get("/")
async def home():
    reply = ("this sentence is already halfway over,"
            " and still hasn't said anything at all")
    return {"message": reply}


@app.post('/model/predict', response_model=Output, response_class=UJSONResponse)
def predict(input: Input):
    return {
        "class_label": model.predict(input.dict())
    }

@app.post("/model/score/{method}", response_model=ScoreOutput, response_class=UJSONResponse)
def score(method: ValidScores, input: ScoreInput):
    data = input.data.dict()
    label = input.label
    method = method.value
    return {
        "score": model.score(data, label, method),
        "method": method
    }
