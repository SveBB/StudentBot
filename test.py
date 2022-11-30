import _pickle as cPickle

def save_model(model, filename):
    with open(filename, 'wb') as fid:
        cPickle.dump(model, fid)

def load_model(filename):
    with open(filename, 'rb') as fid:
        model = cPickle.load(fid)
    return model

clf = load_model('files/NB_classifier.pkl')
vectorizer = load_model('files/vectorizer.pkl')
le = load_model('files/le.pkl')

my_test_data  = [
                 'расписание ммф',
                 'оформить мат помощь',
                 'где находится мед пункт',
                 'ближайший банкомат'
]

my_test_data = vectorizer.transform(my_test_data)
predict_labels = clf.predict(my_test_data)
print(le.inverse_transform(predict_labels))
