# Fisher's Iris Data Set

This repository contains my solutions to the Problem Set for the module Programming and Scripting at GMIT.
[See here for the instructions](https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf)

## What is Fisher's Iris Data Set?

<p>This data set was first introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.[2] For his work in statistics, he has been described as "a genius who almost single-handedly created the foundations for modern statistical science" and "the single most important figure in 20th century statistics".[3] </p>

![Ronald Fisher](/images/RFisher.JPG)

<p>This data set has 150 objects of 3 different classes and 4 features. The 3 different classes of different species of the North American *Iris* flower *Iris setosa, I. virginica* and *I. ersicolor*.[1] It has 50 numeric values for each of the 3 species (in cm); 

1. sepal length 
2. sepal width 
3. petal length 
4. petal width </p>

![Fisher's Iris Data](/images/irisBanner.jpg)

<p>Because it was one of the first widely available and high profile ‘real data’ sets, it’s use increased hugely as a teaching resource for statistics.  It is very often used today for testing out machine learning and visualizations (for example scatter plots).[2] </p>

## Starting the investigation
<p>In order to look at fishers iris data set we must first import the various libraries needed to visualise and investigate the data. The libraries used in this project are; pandas, seaborn and matplotlib 

1. [Pandas](https://pandas.pydata.org/) -  an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools.
2. [Seaborn](https://seaborn.pydata.org/) - is a python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.
3. [Matplotlib](https://matplotlib.org/) - is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms</p>

<p>Next step is to import the dataset:
![Importing Data](/images/readData.PNG)</p>
<p>Now that the data has been imported we can begin to investigate it.
![First entries](/images/headTable.PNG)</p>
<p>As we can see the first 4 variables are measurements in centimeters. All of these flowers were measured in the same location, the same instrument to measure and all taken by the same person so they are consistent. This data was used by Fisher to see if he could identify the type of flower only by taking measurement of the sepals or petals. It must be useful for us to see exactly what sepals and petals are so have a look at this diagram:
![Petals/Sepal Diagram](/images/petal_sepal_label.PNG) </p>
<p>So the petals are the usually coloured part that covers the inner part of the flower. The speals are the usually green base that holds the flowers</p>

## Summary Statistical Table
<p>This is a general overview of statics relating to dataset. </p>
![Summary](/res/table.csv)
<p>From this table the biggest observation we can see is that there is huge variance in the speal length and petal length. Next we will look at boxplots and scatter plots to actually visualise the data</p>

## Box Plots
<p>We will first look at how spread out these values are: 
![General Box Plot](/res/genBoxPlot.jpg)</p>
<p>Sepal length and width seem to be spread fairly evenly amongst their own averages. In comparsion petal lengths and width are far more spread out with alot more values below the averages. We will next look further into the dataset grouping by the specifc flowers in the dataset.</p>
![Box Plot - Petal Length](/res/BoxPlotPetLen.jpg)
![Box Plot - Petal Width](/res/BoxPlotPetWid.jpg)
![Box Plot - Sepal Length](/res/BoxPlotSepLen.jpg)
![Box Plot - Sepal Width](/res/BoxPlotSepWidth.jpg)



## References
1. [UC Irvine Machine Learning Repository: Iris data set](https://archive.ics.uci.edu/ml/datasets/iris)
2. [Wikipedia - Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
3. [Wikipedia - Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher)
4. [Dataset Download](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)
5. [Data36 Pandas Tutorial](https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/)
6. [Geek for Geeks Data Science Tutorial](https://www.geeksforgeeks.org/python-for-data-science/)
7. [Offical Pandas Documentation](http://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.describe.html )
8. [Stack Overflow - Plotting Multiple Histograms](https://stackoverflow.com/questions/29530355/plotting-multiple-histograms-in-grid)
9. [Real Python - Plotting Histograms](https://realpython.com/python-histograms/)
10. [Tutorials Point - Seaborn Tutorial](https://www.tutorialspoint.com/seaborn/index.html)
11. [Offical Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
12. [Stackoverflow - manually making a legend in matplotlib](https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib)
13. [Pandas - Melting DF](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html)
