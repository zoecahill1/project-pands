# Zoe Cahill - Programming and Scripting Project
# Investigations into Fisher's Iris Data Set

# Data Set downloaded from: https://archive.ics.uci.edu/ml/datasets/iris

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

# Using pandas to load data as a dataframe from iris.csv
data = pd.read_csv("res/iris.csv", sep=",")
data1 = pd.read_csv("res/iris.csv", sep=",", header = None, names= ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Flower"])
# Melts data for use in later graphs ref: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html
mData = pd.melt(data1, "Flower", var_name="Features")

def readData():


    # Prints first 5 entries
    print (data.head())
    print ("")

    # Adding column headings as orignal has none and read.csv()
    # takes first line of file as headings
    data1 = pd.read_csv("res/iris.csv", sep=",", header = None, names= ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Flower"])

    # Print 5 sample entries from dataframe to check in
    # correct format
    print (data1.sample(10))
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

def plotSwarmPlot():
    # Sets the size of the graph to aid readablity
    sns.set(rc={'figure.figsize':(10.0,8.0)})

    # Draw a categorical scatterplot
    sns.swarmplot(x="Features", y="value", hue="Flower", data=mData)
    # Title of graph
    plt.title("Swarm Plot of Measurements")
    # Saves the plot
    plt.savefig('res/swarmPlot.jpg')
    # Clears plt for next figure
    plt.close()

# General Box Plot of all features to visualise spread of data
def genBoxPlot():
    # Taking melted data as input
    sns.boxplot(x="Features", y="value",data=mData)
    # Labelling y axis
    plt.ylabel("Measurements in cm")
    # Setting title
    plt.title("Boxplot of Measurements")
    # Saves figure to res file
    plt.savefig("res/genBoxPlot.jpg")
    plt.close()

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

# Pair plot gives us a good overview of the data
# Will generate multiple graphs across all the different variables
def pairPlot():
    # hue will tell sns how to colour code the data 
    sns.pairplot(data1, hue='Flower')
    # saves the graph to res file
    plt.savefig('res/pairplot.jpg')
    # close the file to clear for next figure
    plt.close()

# Generating scatter plots to show that there is distinct difference in sizes between the species
# This function will graph sepal width and sepal length
def scatterSepal():
    # Generating data for x axis
    x = list(data1['Sepal Length (cm)'])
    # Generating data for y axis
    y = list(data1['Sepal Width (cm)'])
    
    # Generating map for different flowers as default will have them all the same colour
    colormap = {'Iris-setosa': 'blue', 'Iris-versicolor': 'red', 'Iris-virginica': 'green'}
    colors = [colormap[x] for x in data1['Flower']]

    # Specifying axis and colors for dataset
    plt.scatter(x, y, c=colors)

    # Labelling x and y axis and specifying title for graph
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.title("Sepal Length and Sepal Width")
    
    # Adapted from: https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
    # Had to manually make legend
    patchList = []
    for key in colormap:
        data_key = mpatches.Patch(color=colormap[key], label=key)
        patchList.append(data_key)

    # Specifying handles and position of legend. Reduced font
    # size to stop legend blocking some data
    plt.legend(handles=patchList, loc='upper left', fontsize= 8)
    # Saving file to res folder
    plt.savefig('res/scatterSepal.jpg') 

# This function will graph petal length and petal width
def scatterPetal():
    x = list(data1['Petal Length (cm)'])
    y = list(data1['Petal Width (cm)'])
    
    colormap = {'Iris-setosa': 'blue', 'Iris-versicolor': 'red', 'Iris-virginica': 'green'}
    colors = [colormap[x] for x in data1['Flower']]

    plt.scatter(x, y, c=colors)

    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Petal Length and Petal Width")
    
    patchList = []
    for key in colormap:
        data_key = mpatches.Patch(color=colormap[key], label=key)
        patchList.append(data_key)

# This function will graph sepal length and petal width
def scatterSepLenPetWid():
    x = list(data1['Sepal Length (cm)'])
    y = list(data1['Petal Width (cm)'])
    
    colormap = {'Iris-setosa': 'blue', 'Iris-versicolor': 'red', 'Iris-virginica': 'green'}
    colors = [colormap[x] for x in data1['Flower']]

    plt.scatter(x, y, c=colors)

    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Sepal Length and Petal Width")
    
    patchList = []
    for key in colormap:
        data_key = mpatches.Patch(color=colormap[key], label=key)
        patchList.append(data_key)

    plt.legend(handles=patchList, loc='upper left', fontsize= 8)
    plt.savefig('res/scatterSepLenPetWid.jpg') 

    plt.legend(handles=patchList, loc='upper left', fontsize= 8)
    plt.savefig('res/scatterPetal.jpg') 

# This function will grpah sepal width to petal length
def scatterSepWidPetLen():
    x = list(data1['Sepal Width (cm)'])
    y = list(data1['Petal Length (cm)'])
    
    colormap = {'Iris-setosa': 'blue', 'Iris-versicolor': 'red', 'Iris-virginica': 'green'}
    colors = [colormap[x] for x in data1['Flower']]

    plt.scatter(x, y, c=colors)

    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.title("Sepal Width and Petal Length")
    
    patchList = []
    for key in colormap:
        data_key = mpatches.Patch(color=colormap[key], label=key)
        patchList.append(data_key)

    plt.legend(handles=patchList, loc='upper left', fontsize= 8)
    plt.savefig('res/scatterSepWidPetLen.jpg') 

