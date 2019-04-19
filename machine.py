from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from sklearn.datasets import load_iris
import seaborn as sns
from graphviz import Source # https://graphviz.readthedocs.io/en/stable/manual.html

def decisionTree():
    iris = sns.load_dataset("iris")
    y = iris.species
    X = iris.drop('species', axis=1)

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


