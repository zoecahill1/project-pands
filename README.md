# Fisher's Iris Data Set

This repository contains my solutions to the Problem Set for the module Programming and Scripting at GMIT.
[See here for the instructions](https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf)

## How to Download the Repository
1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click Clone or download.
3. In the Clone with HTTPs section, click to copy the clone URL for the repository.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 2.
7. Press Enter. Your local clone will be created.

## How to Run the Code
1. Make sure you have python v. 3.7 installed. This can be downloaded here from the [anaconda website.](https://www.anaconda.com/distribution/)
2. Run command line.
3. Navigate to where you have the files saved in your directory.
4. Open start.py and follow instructions in comments to change function name.
5. Type python followed by the start.py to run the program. All functions are in analysis.py and what they do is list above the first line as a comment. All functions in machine.py contain the machine learning code.

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
3. [Matplotlib](https://matplotlib.org/) - is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms
4. [Graphviz](https://graphviz.readthedocs.io/en/stable/manual.html) Graphviz provides a simple pure-Python interface for the Graphviz graph-drawing software. To install this package with anaconda run: conda install -c anaconda graphviz 
5. [numpy](https://www.numpy.org/)NumPy is the fundamental package for scientific computing with Python. It contains among other things; a powerful N-dimensional array object, sophisticated (broadcasting) functions, tools for integrating C/C++ and Fortran code, useful linear algebra, Fourier transform, and random number capabilities
6. [sklearn](https://scikit-learn.org/stable/) is a machine learning library for the Python programming language. It features various classification, regression and clustering algorithms including support vector machines, random forests,gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.


<p>Next step is to import the dataset:

![Importing Data](/images/readData.JPG)</p>

<p>Now that the data has been imported we can begin to investigate it. 

![Head of date](/images/head.JPG)</p>

<p>This code will show the first 10 lines of the dataset [6]

![First entries](/images/headTable.JPG)</p>

<p>As we can see the first 4 variables are measurements in centimeters. All of these flowers were measured in the same location, the same instrument to measure and all taken by the same person so they are consistent. This data was used by Fisher to see if he could identify the type of flower only by taking measurement of the sepals or petals. It must be useful for us to see exactly what sepals and petals are so have a look at this diagram:

![Petals/Sepal Diagram](/images/petal_sepal_label.png) </p>

<p>So the petals are the usually coloured part that covers the inner part of the flower. The speals are the usually green base that holds the flowers[14]</p>

## Summary Statistical Table
<p>The best overview of the data is to generate a table of stastical data which we can easily do with python. [6]

![Python Summary](/images/summary.JPG)</p>

<p>This gives us a good starting point for our investigations.</p>

![Summary](/images/table.JPG)

<p>From this table the biggest observation we can see is that there is huge variance in the speal length and petal length. Next we will look at boxplots and scatter plots to actually visualise the data</p>

## Box Plots
<p>We will first look at how spread out these values are. To do this we can generate a box plot.

![Box Code](/images/genBox.JPG)</p>
**note: for this graph the mData used is "melted" data.
![Melt Data](/images/melt.JPG)
 Melt() function is useful to massage a DataFrame into a format where one or more columns are identifier variables, while all other columns, considered measured variables, are unpivoted to the row axis, leaving just two non-identifier columns, variable and value [15]

![General Box Plot](/res/genBoxPlot.jpg)

<p>Sepal length and width seem to be spread fairly evenly amongst their own averages. In comparsion petal lengths and width are far more spread out with alot more values below the averages. We will next look further into the dataset grouping by the specific flowers in the dataset.</p>

![Box Code](/images/boxM.JPG)

<p>This function plots the various features of the flower against each other [10, 11] </p>

![Box Plot - Petal Length](/res/BoxPlotPetLen.jpg)
![Box Plot - Petal Width](/res/BoxPlotPetWid.jpg)
![Box Plot - Sepal Length](/res/BoxPlotSepLen.jpg)
![Box Plot - Sepal Width](/res/BoxPlotSepWid.jpg)

<p>Looking at all of the plots, we can see that there are distinct differences between the Petal Length and Petal Width. Sepal Length to a lesser extent and sepal width seems to be the most similar across flowers. Each of the different flowers has petal length and width that are very distinct across the various types. They are much closer together for the sepal measurements across the various flowers</p>

## Histograms
<p>Next we will look at some histograms to see can we see anything else within the data. For this graph I had to create a seperate function to group each feature by their flower [8, 9]

![Histogram Code](/images/hist.JPG)
![Grouping Code](/images/group.JPG)</p>

<p>Histograms can help us to see the shape of the distribution of each feature by each flower. This will help us identify any differences between the flowers grouped by their measurements</p>

![Histogram](/res/Histogram.jpg)

<p>From this graph we can see that the setosa seems to have the most distinct features compared to the other two flowers. The setosa also by far has the largest petals (in both width and length). Versicolor and virgincia seem to overlap quite a bit in sepal length and width. There appears to be more of a difference between the two in petal length and width.</p>

## Swarm Plot
<p>Another good way to get an overview of the data is with a swarm plot. A swarm plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.</p>

![Swarm Code](/images/swarm.JPG)

<p>This gives us a good overview of the spread of data</p>

![Swarm Plot](/res/swarmPlot.jpg)

<p>We can clearly see here that Iris-virginica is the largest flower as it is a the top or nearly the top in each swarm. Also we can see petals have a much bigger difference between then as opposed to the speal measurements.</p>

## Pair Plot
<p>Next we will try to take a look at how some of these variables interact. An easy way to get a good overview of this is with a pairplot</p>

![Pair Plot Code](/images/pair.JPG)

<p>This gives us a great overview and allows us to better visualise the data thereby allowing us to make important observations about the data.</p>

![Pair Plot](/res/pairplot.jpg)

<p>Let's look a little but closer a some of these scatter plots</p>

## Scatter Plots
<p>Firstly we will look at whether there is any relationship between sepal length and width. Coding this was a little tricky. I had to create a colourmap to make the graph readable and then maunally make a legend rather than have the computer generate one [12]</p>

![Scatter Sepal Code](/images/scatterSepal.JPG)

<p>Look at the scatter plots we can make some observations about the data</p>

![Scatter Speal](/res/scatterSepal.jpg)

<p>Iris-Setosa appears to be the only flower that differs in a distinctive way in terms of speal length and width. However Iris-versicolor and Iris-virginica appear a little more varied and mixed together</p>

<p>Next we will look at the relationship between petal length and width. Coding this was much the same processs as the previous graph.</p>

![Scatter Petal](/images/scatterPetal.JPG)

<p>So looking at the relationship between petal length and width we can make some observations.</p>

![Petal Plot](/res/scatterPetal.jpg)

<p>Examining the graph tells us that these two measurements increase together. Logically that must be true if they did not they would be very long thin petals, or else very short and wide petals. The graph also shows that this is a very good way to differinate between the different flowers</p>







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
14. [Wikipedia - Flowers](https://en.wikipedia.org/wiki/Sepal)
15. [Geek for Geeks - Melt()](https://www.geeksforgeeks.org/python-pandas-melt/)
16. [Exploring the Iris Dataset](https://medium.com/@livingwithdata/exploring-the-iris-dataset-260cc1e5cdf7)
17. [Kaggle - scikit learn video](http://blog.kaggle.com/2015/04/22/scikit-learn-video-3-machine-learning-first-steps-with-the-iris-dataset/)
18. [Machine Learning on Iris](https://diwashrestha.com/2017/09/18/machine-learning-on-iris/)
19. [Seaborn - Swarm Plots](https://seaborn.pydata.org/generated/seaborn.swarmplot.html)
20. [Graphviz user guide](https://graphviz.readthedocs.io/en/stable/manual.html)
21. [Stackoverflow - plotting graph from dot file](https://stackoverflow.com/questions/41942109/plotting-the-digraph-with-graphviz-in-python-from-dot-file)
22. [KKN - Iris Dataset](https://www.kaggle.com/nautna/iris-knn-python-classification)