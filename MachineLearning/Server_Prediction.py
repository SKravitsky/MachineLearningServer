import numpy as np
import pandas as pd
import os
import sys
import pydot
import mysql.connector
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals.six import StringIO


config = {
  'user': 'ECE32',
  'password': 'seniordesign',
  'host': 'septa-instance.ctejk6luw06s.us-west-2.rds.amazonaws.com',
  'database': 'septa',
  'raise_on_warnings': True,
}


def get_alllines():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)

    df_mysql = pd.read_sql('select * from VIEWS;', con=cnx)

    '''
    cursor.execute("SELECT * FROM septa.lines")

    lines = {}
    for row in cursor:
        line_id = row['id']
        lines[row['name']] = line_id

    cursor.close()
    cnx.close()

    return lines
    '''


def get_csv():
    if os.path.exists("Update.csv"):
        df = pd.read_csv("Update.csv")
    return df

def scrub_df(data):
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

    #tree.export_graphviz(clf, out_file='tree.dot', feature_names=N, filled=True, rounded=True)
    #os.system('dot -Tpng tree.dot -o tree.png')

if __name__ == "__main__":
    df = get_csv()
    features, targets, names = scrub_df(df)
    prediction(features, targets, names)
