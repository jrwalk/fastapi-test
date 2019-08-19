from typing import List

import cloudpickle as pickle
import numpy as np
import pandas
import sklearn.metrics as metrics


class ModelWrapper:
    def __init__(self, model_path: str):
        with open(model_path, "rb") as rf:
            self.model = pickle.load(rf)

    def predict(self, X: dict) -> List[int]:
        X = pandas.DataFrame(X)
        return self.model.predict(X).tolist()

    def score(self, X: dict, y: List[int], method: str) -> float:
        X = pandas.DataFrame(X)
        scorer = metrics.get_scorer(method)
        return scorer(self.model, X, y)
