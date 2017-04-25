import numpy as np
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

train_feature = np.genfromtxt('feature.csv', delimiter=',', dtype=int)
train_temp = np.genfromtxt('target.csv', delimiter=',', dtype=int)
train_target = np.vstack((train_temp))


clf = tree.DecisionTreeClassifier()
clf.fit(train_feature, train_target)
#clf.predict(test_data)

tree.export_graphviz(clf,
            feature_names=('Week','Day','Time','Station'),
            class_names=('Prediction'),
            filled=True,
            rounded=True,
            out_file='tree.dot')
