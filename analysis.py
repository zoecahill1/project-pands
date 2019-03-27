# Zoe Cahill - Programming and Scripting Project
# Investigations into Fisher's Iris Data Set

# Data Set downloaded from: https://archive.ics.uci.edu/ml/datasets/iris

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Writes table to csv file
table.to_csv("res/table.csv")
