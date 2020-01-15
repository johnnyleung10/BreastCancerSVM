import sklearn
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import metrics
import pickle

#Obtain Data
cancer_data = pd.read_csv("breast-cancer-wisconsin.data")


#Remove ID from data
cancer_data = cancer_data[["clump_thickness", "uni_cell_size", "uni_cell_shape", "adhesion", "single_cell_size",
                           "chromatin", "normal_nucleoli", "mitosis", "class"]]

# Prediction will be "class" which indicates if benign or malignant
predict = "class"

X = np.array(cancer_data.drop([predict], 1)) # Features
Y = np.array(cancer_data[predict]) # Labels

# Create train and testing sets
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)


# TRAIN FOR BEST ACC (Best is saved in "breast-cancer-model.pickle")
'''
best = 0
for _ in range(100):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)
    clf = svm.SVC(kernel="linear", C=3)
    clf.fit(x_train, y_train)

    accuracy = metrics.accuracy_score(y_test, y_pred)
    print("Accuracy: ", round(accuracy * 100, 2), "%")

    if accuracy > best:
        best = accuracy
        with open("breast-cancer-model.pickle", "wb") as f:
            pickle.dump(clf, f)
'''

# Load best model
pickle_in = open("breast-cancer-model.pickle", "rb")
clf = pickle.load(pickle_in)

y_pred = clf.predict(x_test)

for x in range(len(y_pred)):
    predicted_tumor = ""
    actual_tumor = ""

    if y_pred[x] == 2:
        predicted_tumor = "Benign"
    elif y_pred[x] == 4:
        predicted_tumor = "Malignant"

    if y_test[x] == 2:
        actual_tumor = "Benign"
    elif y_test[x] == 4:
        actual_tumor = "Malignant"

    print("******************************")
    print("Prediction: ", predicted_tumor, "\nData: ", x_test[x], "\nActual: ", actual_tumor)
    print("******************************")







