import numpy as np
import pandas as pd
import os
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals.six import StringIO
import pydot

def get_csv():
    if os.path.exists("Update2.csv"):
        df = pd.read_csv("Update2.csv")
    return df

def scrub_csv(data):
    #print("* df.head()", data.head())
    
    features = list(df.columns[:3])
    
    #print("* features:", features)

    X = df[features]
    Y = df["Prediction"]

    #print("Head", X.tail())
    #print("Head2", Y.tail())
    
    return X,Y,features

def prediction(F, T, N):
    clf = tree.DecisionTreeClassifier()

    F_train, F_test, T_train, T_test = train_test_split(F, T, test_size = .2)

    clf.fit(F_train, T_train)
    predictions = clf.predict(F_test)
    
    print accuracy_score(T_test, predictions)
    
    class_names_tree = clf.classes_
    temp = class_names_tree.tolist()

    for x,y in enumerate(temp):
        temp[x] = str(y)
        print type(temp[x])

    tree.export_graphviz(clf, out_file='tree.dot', feature_names=N, class_names=temp, filled=True, rounded=True)
    os.system('dot -Tpng tree.dot -o tree.png')

if __name__ == "__main__":
    df = get_csv()
    features, targets, names = scrub_csv(df)
    prediction(features, targets, names)
