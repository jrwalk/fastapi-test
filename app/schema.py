from pydantic import BaseModel
from enum import Enum
from typing import List


class Input(BaseModel):
    sepal_length: List[float]
    sepal_width: List[float]
    petal_length: List[float]
    petal_width: List[float]


class Output(BaseModel):
    class_label: List[int]


class ScoreInput(BaseModel):
    data: Input
    label: List[int]


class ScoreOutput(BaseModel):
    score: float
    method: str


class ValidScores(str, Enum):
    accuracy = "accuracy"
