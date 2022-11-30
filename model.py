import _pickle as cPickle


class Model():
    def __init__(self, path_to_clf, path_to_vectorizer, path_to_le):
        self._clf = self._load_model(path_to_clf)
        self._vectorizer = self._load_model(path_to_vectorizer)
        self._le = self._load_model(path_to_le)

    def _load_model(self, filename):
        with open(filename, 'rb') as fid:
            model = cPickle.load(fid)
        return model

    def predict(self, message: str):
        data = self._vectorizer.transform(message)
        predict_label = self._clf.predict(data)
        response = self._le.inverse_transform(predict_label)
        return response
