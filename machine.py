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

# loading iris dataset from seaborn as it comes preloaded in package
iris = sns.load_dataset("iris")
y = iris.species
# drop column species for testing
X = iris.drop('species', axis=1)

# function to generate decision tree
def decisionTree():
    # split data into training and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size = 0.3, 
                                                        random_state = 100, 
                                                        stratify = y)

    # decision tree classifier
    clf = tree.DecisionTreeClassifier()
    # fit training data (X_train and y_train) to train the model
    clf.fit(X_train,y_train)

    # the decision_tree classifier makes a tree which will classify the
    # species of test data.
    iris2 = load_iris()

    # The decision tree is then created and output to a dot file
    # which can be visualised using graphviz
    #tree.export_graphviz(clf, 
    #out_file='res/iris.dot', feature_names=iris2.feature_names, 
                                                #class_names=iris2.target_names, 
                                                #filled=True, 
                                                #rounded=True, 
                                                #special_characters=True)

    # prediction from our model with X_test as the passed data
    y_pred = (clf.predict(X_test))

    # generates a score telling us how accurate the predictions are
    print("Accuracy Score: {:.2f}%".format(accuracy_score(y_test, y_pred)*100))

# Function to view the dot file in graphviz
# Adapted from: https://stackoverflow.com/questions/41942109/plotting-the-digraph-with-graphviz-in-python-from-dot-file
def view():
    # declaring the file path
    path = 'res/iris.dot'
    # setting the file path variable
    s = Source.from_file(path)
    # viewing the file
    s.view()

# Function to test using kk-N algorithim
# Adapted from: https://www.kaggle.com/nautna/iris-knn-python-classification
def kknTest():
    # again we split data into training and test sets.
    # Here we set the random state to 0 for reproducibility 
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        random_state = 0)
    
    # This will show us how our data has been split
    print("X_train shape: {}\ny_train shape: {}".format(X_train.shape, y_train.shape))
    print("X_test shape: {}\ny_test shape: {}".format(X_test.shape, y_test.shape))

    # This varibale is setting the estimator object. 
    # An estimator is any object that learns from data; it may be a classification, 
    # regression or clustering algorithm or a transformer that extracts/filters useful features from raw data.
    # https://scikit-learn.org/stable/tutorial/statistical_inference/settings.html
    knn = KNeighborsClassifier(n_neighbors=1)

    # Then we fit the model with the training set in order to predict classes
    knn.fit(X_train, y_train)

    # prediction from our model with X_test as the passed data
    y_pred = knn.predict(X_test)

    # based on the training dataset, our model predicts the following for the test set:
    table = pd.concat([X_test, y_test, pd.Series(y_pred, name='Predicted', index=X_test.index)], ignore_index=False, axis=1)
    print (table)
    # generates a score telling us how accurate the predictions are
    print("Accuracy Score: {:.2f}%".format(knn.score(X_test, y_test)*100))


