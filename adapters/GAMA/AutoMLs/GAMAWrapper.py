from sklearn.base import BaseEstimator, ClassifierMixin #Need or else dashboard will thing no predict_proba exists, only an issue with evalml and gama
from BaseWrapper import BaseWrapper

class GAMAWrapper(BaseEstimator, ClassifierMixin, BaseWrapper):

    def __init__(self, model, config) -> None:
        super().__init__(model, config)

    def predict(self, X, **kwargs):
        X_predict = self._prepare_dataset(X)
        return self._model.predict(X_predict)

    def predict_proba(self, X, **kwargs):
        X_predict = self._prepare_dataset(X)
        return self._model.predict_proba(X_predict).tolist()
