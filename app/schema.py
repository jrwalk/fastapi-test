from typing import List
from enum import Enum

from pydantic import BaseModel


class Record(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class LabeledRecord(BaseModel):
    record: Record
    label: int


class Input(BaseModel):
    data: List[Record]


class LabeledInput(BaseModel):
    data: List[LabeledRecord]


class Prediction(BaseModel):
    class_label: List[int]


class Score(BaseModel):
    score: float
    method: str


class ValidScores(str, Enum):
    accuracy = "accuracy"
