# Zoe Cahill - Programming and Scripting Project
# Investigations into Fisher's Iris Data Set

# Data Set downloaded from: https://archive.ics.uci.edu/ml/datasets/iris

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, output_file, show

# Using pandas to load data as a dataframe from iris.csv
data = pd.read_csv("res/iris.csv", sep=",")
data1 = pd.read_csv("res/iris.csv", sep=",", header = None, names= ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Flower"])

def readData():


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
    # This function will create histograms of the examined features grouped by flower.  
    # This will help us to idenitify differences between each flower by their features. 

    # Produce a list called columns from the column headings in the data frame to iterate through with enumerate
    columns = list(data1[['Sepal Width (cm)','Sepal Length (cm)','Petal Width (cm)','Petal Length (cm)']])

    # Adapted from https://stackoverflow.com/questions/29530355/plotting-multiple-histograms-in-grid
    # For statement to produce multiple histograms in a grid.
    # To do this we use a for statement and the enumerate function to 
    # loop over the columns list and have a counter with the group by function colHist()
    for i, alpha in enumerate(columns):
        # (num_of_rows, num_of_columns, i + 1)
        # Adapted from: https://realpython.com/python-histograms/
        plt.subplot(2, 2, i + 1)
        # Plots histogram on lists from called function
        plt.hist(colHist(alpha)[0], alpha=0.6, label='setosa')
        plt.hist(colHist(alpha)[1], alpha=0.6, label='versicolor')
        plt.hist(colHist(alpha)[2], alpha=0.6, label='virginica')
        # Reduced font size to avoid blocking graph data
        plt.legend(loc='upper right', fontsize=6)
        # X and Y labels
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
    # So we must group these by flower
    setosa = data1[data1['Flower'] == 'Iris-setosa'][col]
    versicolor = data1[data1['Flower'] == 'Iris-versicolor'][col]
    virginica = data1[data1['Flower'] == 'Iris-virginica'][col]
    return setosa, versicolor, virginica

# Function to plot box plots for various features
# Refrenced throughout:
# https://www.tutorialspoint.com/seaborn/index.html
# https://seaborn.pydata.org/tutorial.html
def plotBoxPlot():

    # Adding white grid for readablity
    sns.set(style="whitegrid")

    # Plot boxplot using type of flowers for x and sepal length for y.
    sns.boxplot(x="Flower", y="Sepal Length (cm)", data=data1)

    title = "Distributions of Sepal Length"
    # Increased font size for readablity
    plt.title(title, fontsize=20)

    # Saves the plot
    plt.savefig('res/BoxPlotSepLen.jpg')
    # Clears plt for next figure
    plt.close()

    # Box Plot for Sepal Width
    sns.set(style="whitegrid")
    sns.boxplot(x="Flower", y="Sepal Width (cm)", data=data1)
    title = "Distributions of Sepal Width"
    plt.title(title, fontsize=20)
    plt.savefig('res/BoxPlotSepWid.jpg')
    plt.close()

    # Box Plot for Petal Length
    sns.set(style="whitegrid")
    sns.boxplot(x="Flower", y="Petal Length (cm)", data=data1)
    title = "Distributions of Petal Length"
    plt.title(title, fontsize=20)
    plt.savefig('res/BoxPlotPetLen.jpg')
    plt.close()

    # Box Plot for Petal Width
    sns.set(style="whitegrid")
    sns.boxplot(x="Flower", y="Petal Width (cm)", data=data1)
    title = "Distributions of Petal Width"
    plt.title(title, fontsize=20)
    plt.savefig('res/BoxPlotPetWid.jpg')
    plt.close()

# in progress
def plotCurves():

    sns.FacetGrid(data1, hue='Flower', size=6) \
    .map(sns.kdeplot, 'Sepal Length (cm)') \
    .add_legend()

    sns.FacetGrid(data1, hue='Flower', size=6) \
    .map(sns.kdeplot, 'Sepal Width (cm)') \
    .add_legend()

    sns.FacetGrid(data1, hue='Flower', size=6) \
    .map(sns.kdeplot, 'Petal Length (cm)') \
    .add_legend()

    sns.FacetGrid(data1, hue='Flower', size=6) \
    .map(sns.kdeplot, 'Petal Width (cm)') \
    .add_legend()

    plt.show()

# Using bokeh library to generate scatter plot of 
# Had difficulty using plt.scatter bokeh was much easier to use
# And to style, although could not get legend to show so for refrence
# setosa = blue, versicolor = red, virginica = green
# https://bokeh.pydata.org/en/latest/docs/user_guide.html

# Comparing Petal Width and Petal Length of different flowers
def plotScatterPetals():
    output_file("res/scatterPlotPetals.html")

    # Adding colours to various flowers as default is all the same colour
    colormap = {'Iris-setosa': 'blue', 'Iris-versicolor': 'red', 'Iris-virginica': 'green'}
    colors = [colormap[x] for x in data1['Flower']]

    # Setting title and x, y axis labels
    graph = figure(title = "Petal Width and Petal Length")
    graph.xaxis.axis_label = 'Petal Length (cm)'
    graph.yaxis.axis_label = 'Petal Width (cm)'

    # Graphing the data - increased the dot size for readablity
    # Refrenced: https://bokeh.pydata.org/en/latest/docs/reference/models/markers/circle.html
    graph.circle(data1["Petal Length (cm)"], data1["Petal Width (cm)"], size = 12, color=colors)

    # Will generate a HTML file with graph
    # For simplicity I screenshot the results for use in analysis later
    # Note the html file is an interactive graph which can be very useful for other
    # data sets but for our purposes that interaction is not necessary
    show(graph)

# Comparing Sepal Width and Speal Length of different flowers
def plotScatterSepals():
    output_file("res/scatterPlotSepals.html")

    colormap = {'Iris-setosa': 'blue', 'Iris-versicolor': 'red', 'Iris-virginica': 'green'}
    colors = [colormap[x] for x in data1['Flower']]

    graph = figure(title = "Sepal Width and Sepal Length")
    graph.xaxis.axis_label = 'Sepal Length (cm)'
    graph.yaxis.axis_label = 'Sepal Width (cm)'

    graph.circle(data1["Sepal Length (cm)"], data1["Sepal Width (cm)"], size = 12, color=colors)

    show(graph)

# Comparing Sepal Width and Petal Length of different flowers
def plotScatterSepWidPetLen():
    output_file("res/scatterPlotSepWidPetLen.html")

    colormap = {'Iris-setosa': 'blue', 'Iris-versicolor': 'red', 'Iris-virginica': 'green'}
    colors = [colormap[x] for x in data1['Flower']]

    graph = figure(title = "Sepal Width and Petal Length")
    graph.xaxis.axis_label = 'Sepal Width (cm)'
    graph.yaxis.axis_label = 'Petal Length (cm)'

    graph.circle(data1["Sepal Width (cm)"], data1["Petal Length (cm)"], size = 12, color=colors)

    show(graph)


# Comparing Sepal Length and Petal Width of different flowers
def plotScatterSepLenPetWid():
    output_file("res/scatterPlotSepLenPetWid.html")

    colormap = {'Iris-setosa': 'blue', 'Iris-versicolor': 'red', 'Iris-virginica': 'green'}
    colors = [colormap[x] for x in data1['Flower']]

    graph = figure(title = "Sepal Length and Petal Width")
    graph.xaxis.axis_label = 'Sepal Length (cm)'
    graph.yaxis.axis_label = 'Petal Width (cm)'

    graph.circle(data1["Sepal Length (cm)"], data1["Petal Width (cm)"], size = 12, color=colors)

    show(graph)