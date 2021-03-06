from fastapi import FastAPI
from starlette.responses import UJSONResponse

from app.schema import Input, LabeledInput, Prediction, Score, ValidScores
from app.model import ModelWrapper


app = FastAPI(
    title="fastapi-test",
    description="a quick skateboard for serving `sklearn` models with FastAPI",
    version="0.1"
)
model = ModelWrapper("/opt/fastapi-test/models/model.pkl")


@app.get("/")
async def home():
    reply = (
        "this sentence is already halfway over,"
        " and still hasn't said anything at all"
    )
    return {"message": reply}


@app.post("/model/predict", response_model=Prediction, response_class=UJSONResponse)
async def predict(input: Input):
    return {"class_label": model.predict(input.dict()['data'])}


@app.post(
    "/model/score/{method}", response_model=Score, response_class=UJSONResponse
)
async def score(method: ValidScores, input: LabeledInput):
    input = input.dict()['data']
    data = [r['record'] for r in input]
    label = [r['label'] for r in input]
    method = method.value
    return {"score": model.score(data, label, method), "method": method}
