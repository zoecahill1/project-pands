from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import numpy as np
import pandas as pd
from graphviz import Source # https://graphviz.readthedocs.io/en/stable/manual.html

iris = sns.load_dataset("iris")
y = iris.species
X = iris.drop('species', axis=1)

def decisionTree():
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size = 0.3, 
                                                        random_state = 100, 
                                                        stratify = y)

    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train,y_train)

    #DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,max_features=None, max_leaf_nodes=None,min_impurity_split=1e-07, min_samples_leaf=1,min_samples_split=2, min_weight_fraction_leaf=0.0,presort=False, random_state=None, splitter='best')

    iris2 = load_iris()

    #tree.export_graphviz(clf, 
    #out_file='res/iris.dot', feature_names=iris2.feature_names, 
                                                #class_names=iris2.target_names, 
                                                #filled=True, 
                                                #rounded=True, 
                                                #special_characters=True)

    y_pred = (clf.predict(X_test))

    print ('Accuracy Score')
    print (accuracy_score(y_test, y_pred)* 100)

# https://stackoverflow.com/questions/41942109/plotting-the-digraph-with-graphviz-in-python-from-dot-file
def view():
    path = 'res/iris.dot'
    s = Source.from_file(path)
    s.view()


#https://www.kaggle.com/nautna/iris-knn-python-classification
def kknTest():
    # split data into training and test sets; set random state to 0 for reproducibility 
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        random_state = 0)
    
    # see how data has been split
    print("X_train shape: {}\ny_train shape: {}".format(X_train.shape, y_train.shape))
    print("X_test shape: {}\ny_test shape: {}".format(X_test.shape, y_test.shape))

        # initialize the Estimator object
    knn = KNeighborsClassifier(n_neighbors=1)

    # fit the model to training set in order to predict classes
    knn.fit(X_train, y_train)

    # create a prediction array for our test set
    y_pred = knn.predict(X_test)

    # based on the training dataset, our model predicts the following for the test set:
    table = pd.concat([X_test, y_test, pd.Series(y_pred, name='Predicted', index=X_test.index)], ignore_index=False, axis=1)
    print (table)
    print("Test set score: {:.2f}%".format(knn.score(X_test, y_test)*100))


