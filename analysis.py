# Zoe Cahill - Programming and Scripting Project
# Investigations into Fisher's Iris Data Set

# Data Set downloaded from: https://archive.ics.uci.edu/ml/datasets/iris

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv("res/iris.csv", sep=",", header = None, names= ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Flower"])

def readData():
    # Using pandas to load data as a dataframe from iris.csv
    data = pd.read_csv("res/iris.csv", sep=",")

    # Prints first 5 entries
    print (data.head())
    print ("")

    # Adding column headings as orignal has none and read.csv()
    # takes first line of file as headings
    data1 = pd.read_csv("res/iris.csv", sep=",", header = None, names= ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Flower"])

    # Print 5 sample entries from dataframe to check in
    # correct format
    print (data1.sample(5))
    print ("")

def describeData():
    # Prints the total number of entries in the dataframe
    # print ("Total number of entries:", data1.Flower.count())

    # Shape will count the number of rows and columns in the dataset
    shape = data1.shape
    print ("The data set has", shape[0], "rows and", shape[1], "columns" )
    print("")

    # Lists the specific data types of each column
    # This data type object (dtype) informs us about the layout of the array
    print ("Each columns data type is listed as follows: " )
    print (data1.dtypes)
    print ("")

def listSpecies():
    # Values_counts counts the distinct entries in the column Flowers
    print("List of the different species and how many entries each has: ")
    print( data1["Flower"].value_counts())

    # Shows summary of statistical data for dataframe 
    # For numeric data, the result’s index will include count, mean, std, min, max 
    # as well as lower, 50 and upper percentiles. 
    # By default the lower percentile is 25 and the upper percentile is 75. 
    # The 50 percentile is the same as the median.
    table = data1.describe()
    print ("")
    print ("Summary of statistical data")
    print(table)
    # Writes results to csv file
    table.to_csv("res/table.csv")

def plotHistogram():
    # This function will create histograms of  the examined alphas grouped by flower.  
    # This will help us to idenitify differences between each flower by their features. 

    # Produce a list called columns of the column headings to iterate through with enumerate
    columns = list(data1[['Sepal Width (cm)','Sepal Length (cm)','Petal Width (cm)','Petal Length (cm)']])

    # Adapted from https://stackoverflow.com/questions/29530355/plotting-multiple-histograms-in-grid
    # For statement to produce multiple histograms in a grid.

    for i, alpha in enumerate(columns):
        # (num_of_rows, num_of_columns, i + 1)
        plt.subplot(2, 2, i + 1)
        plt.hist(colHist(alpha)[0], alpha=0.6, label='setosa')
        plt.hist(colHist(alpha)[1], alpha=0.6, label='versicolor')
        plt.hist(colHist(alpha)[2], alpha=0.6, label='virginica')
        plt.legend(loc='upper right', fontsize=6)
        plt.xlabel("Measurements in cm")
        plt.ylabel("Number of flowers")
        plt.title(alpha)
    # Improves spacing of graphs otherwise they overlap
    plt.tight_layout(pad=0.5, w_pad=0.5, h_pad=1.0)
    # Save figure to res file
    plt.savefig('res/Histogram.jpg') 
    # Closes generator for next figure to be drawn
    plt.close()

# Function to group each feature by their flower
def colHist(col):
    # The features we will graph as petal length and width, sepal length and width
    # So
    setosa = data1[data1['Flower'] == 'Iris-setosa'][col]
    versicolor = data1[data1['Flower'] == 'Iris-versicolor'][col]
    virginica = data1[data1['Flower'] == 'Iris-virginica'][col]
    return setosa, versicolor, virginica



