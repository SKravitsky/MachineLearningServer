import numpy as np
import pandas as pd
import os
import sys
import pydot
import rds_config
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


def get_all_lines(user_id):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)

    sql4 = 'SELECT id_weekday, time_departure, id_station_origin, id_station_destination FROM trips WHERE id_user = "%s"' % user_id
    sql = 'SELECT id_weekday, time_departure, id_station_origin, id_station_destination FROM trips'


    df_mysql = pd.read_sql(sql, con=cnx)

    #print df_mysql.dtypes

    df_mysql.time_departure = df_mysql.time_departure.astype(int)

    #print df_mysql.dtypes
    #print df_mysql.head()
    return df_mysql
    

def get_csv():
    if os.path.exists("Update.csv"):
        df = pd.read_csv("Update.csv")
    return df


def scrub_df(data):
    #print("* df.head()", data.head())
    
    features = list(data.columns[:3])
    targets = list(data.columns[3:])
    
    #print("* features:", features)
    #print("* targets:", targets)


    X = data[features]
    Y = data[targets]

    #print("Head", X.tail())
    #print("Head2", Y.tail())
    
    return X,Y,features,targets


def prediction_accuracy(F, T, FN, TN):
    clf = tree.DecisionTreeClassifier()

    F_train, F_test, T_train, T_test = train_test_split(F, T, test_size = .2)

    clf.fit(F, T)
    predictions = clf.predict(F_test)
    
    print accuracy_score(T_test, predictions)

    #tree.export_graphviz(clf, out_file='tree.dot', feature_names=FN, filled=True, rounded=True)
    #os.system('dot -Tpng tree.dot -o tree.png')


def prediction(F, T, FN, TN, data):
    clf = tree.DecisionTreeClassifier()
    clf.fit(F, T)

    df_api = pd.DataFrame(data, columns = ['id_weekday','time_departure','id_station_origin'])
    df_api.time_departure = df_api.time_departure.astype(int)

    prediction = clf.predict(df_api)
    
    return prediction


def start_function(user_id, weekday, time, station):
    
    df = get_all_lines(user_id)

    features, targets, fnames, tnames = scrub_df(df)

    data = (weekday, time, station)
    
    #print features
    #prediction_accuracy(features, targets, fnames, tnames)
    
    output_prediction = prediction(features, targets, fnames, tnames, data)
    print output_prediction


def lambda_handler(event, context):
    
    user_id = event['key1']
    weekday = event['key2']
    time = event['key3']
    station = event['key4']

    start_function(user_id, weekday, time, station) 


if __name__ == "__main__":
    user_id = 'e2f4uovEeYU'

    df = get_all_lines(user_id)
    features, targets, fnames, tnames = scrub_df(df)
    print features
    
    '''
    df2 = get_csv()
    features2, targets2, fnames2, tnames2 = scrub_df(df2)
    print '----'
    print features2
    '''

    prediction_accuracy(features, targets, fnames, tnames)
