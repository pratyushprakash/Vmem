from sklearn import linear_model
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier

from collect import get_data

affected_syscalls = [9]


def prep(path):
    data, features = get_data(path)
    features.sort()
    label = []
    new_data = []
    for l in data:
        new_row = []
        if l[0] in affected_syscalls:
            label.append(1)
        else:
            label.append(0)

        memfreq = l[1]
        for f in features:
            if f not in memfreq.keys():
                new_row.append(0)
            else:
                new_row.append(memfreq[f])

        new_data.append(new_row)

    return new_data, label


def logistic_regression(train_data, labels):
    logreg = linear_model.LogisticRegression(C=1e-2)
    logreg.fit(train_data, labels)

    return logreg


def svm(train_data, labels):
    lsvc = LinearSVC(C=0.01, penalty='l1', dual=False)
    lsvc.fit(train_data, labels)

    return lsvc


def random_forest(train_data, labels):
    rforest = RandomForestClassifier()
    rforest.fit(train_data, labels)

    return rforest


def test(path):
    data, label = prep(path)
    train_data = data[:-1]
    x = []
    for row in train_data:
        if len(row) not in x:
            x.append(len(row))

    print(x)
    logreg = logistic_regression(train_data, label[:-1])
    lsvc = svm(train_data, label[:-1])
    rforest = random_forest(train_data, label[:-1])
    
    logreg_result = logreg.predict([data[-2]])
    lsvc_result = lsvc.predict([data[-2]])
    rforest_result = rforest.predict([data[-2]])
    
    print('Result - logistical regression: {}'.format(logreg_result))
    print('Result - Support Vector Machines: {}'.format(lsvc_result))
    print('Result - Random Forest Classifier: {}'.format(rforest_result))
