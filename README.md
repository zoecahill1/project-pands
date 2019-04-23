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

<p>This data set has 150 objects of 3 different classes and 4 features. The 3 different classes of different species of the North American Iris flower Iris setosa, I. virginica and I. ersicolor.[1] It has 50 numeric values for each of the 3 species (in cm); 

1. sepal length 
2. sepal width 
3. petal length 
4. petal width </p>

![Fisher's Iris Data](/images/irisBanner.jpg)

<p>Because it was one of the first widely available and high profile ‘real data’ sets, it’s use increased hugely as a teaching resource for statistics.  It is very often used today for testing out machine learning and visualizations (for example scatter plots).[2] </p>

## Starting the investigation
<p>In order to look at fishers iris data set we must first import the various libraries needed to visualise and investigate the data. The libraries used in this project are; pandas, seaborn, matplotlib, graphviz, numpy and sklearn.

1. [Pandas](https://pandas.pydata.org/) -  an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools.
2. [Seaborn](https://seaborn.pydata.org/) - is a python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.
3. [Matplotlib](https://matplotlib.org/) - is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms
4. [Graphviz](https://graphviz.readthedocs.io/en/stable/manual.html) - Graphviz provides a simple pure-Python interface for the Graphviz graph-drawing software. To install this package with anaconda run: conda install -c anaconda graphviz 
5. [numpy](https://www.numpy.org/) - NumPy is the fundamental package for scientific computing with Python. It contains among other things; a powerful N-dimensional array object, sophisticated (broadcasting) functions, tools for integrating C/C++ and Fortran code, useful linear algebra, Fourier transform, and random number capabilities
6. [sklearn](https://scikit-learn.org/stable/) - is a machine learning library for the Python programming language. It features various classification, regression and clustering algorithms including support vector machines, random forests,gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.


<p>Next step is to import the dataset:

![Importing Data](/images/readData.JPG)</p>

<p>Now that the data has been imported we can begin to investigate it. 

![Head of date](/images/head.JPG)</p>

<p>This code will show the first 10 lines of the dataset [6]

![First entries](/images/headTable.JPG)</p>

<p>As we can see the first 4 variables are measurements in centimeters. All of these flowers were measured in the same location, the same instrument to measure and all taken by the same person so they are consistent. This data was used by Fisher to see if he could identify the type of flower only by taking measurement of the sepals or petals.[2] It must be useful for us to see exactly what sepals and petals are so have a look at this diagram:

![Petals/Sepal Diagram](/images/petal_sepal_label.png) </p>

<p>So the petals are the usually coloured part that covers the inner part of the flower. The speals are the usually green base that holds the flowers[14]</p>

## Summary Statistical Table
<p>The best overview of the data is to generate a table of stastical data which we can easily do with python. [6]

![Python Summary](/images/summary.JPG)</p>

<p>This gives us a good starting point for our investigations.</p>

![Summary](/images/table.JPG)

<p>From this table the biggest observation we can see is that there is huge variance in the speal length and petal length. Next we will look at boxplots and scatter plots to actually visualise the data.</p>

## Box Plots
<p>We will first look at how spread out these values are. To do this we can generate a box plot.

![Box Code](/images/genBox.JPG)</p>
**note: for this graph the mData used is "melted" data.
![Melt Data](/images/melt.JPG)
 Melt() function is useful to massage a DataFrame into a format where one or more columns are identifier variables, while all other columns, considered measured variables, are unpivoted to the row axis, leaving just two non-identifier columns, variable and value [15]

![General Box Plot](/res/genBoxPlot.jpg)

<p>Sepal length and width seem to be spread fairly evenly amongst their own averages. In comparsion petal lengths and width are far more spread out with alot more values below the averages.</p> 

<p>Next, we will look further into the dataset grouping by the specific flowers in the dataset.</p>

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
<p>Another good way to get an overview of the data is with a swarm plot. A swarm plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.[19]</p>

![Swarm Code](/images/swarm.JPG)

<p>This gives us a good overview of the spread of data</p>

![Swarm Plot](/res/swarmPlot.jpg)

<p>We can clearly see here that Iris-virginica is the largest flower as it is a the top or nearly the top in each swarm. Also we can see petals have a much bigger difference between then as opposed to the speal measurements.</p>

## Pair Plot
<p>Next we will try to take a look at how some of these variables interact. An easy way to get a good overview of this is with a pairplot:</p>

![Pair Plot Code](/images/pair.JPG)

<p>This gives us a great overview and allows us to better visualise the data thereby allowing us to make important observations about the data.</p>

![Pair Plot](/res/pairplot.jpg)

<p>Let's look a little but closer a some of these scatter plots.</p>

## Scatter Plots
<p>Firstly we will look at whether there is any relationship between sepal length and width. Coding this was a little tricky. I had to create a colourmap to make the graph readable and then maunally make a legend rather than have the computer generate one.[12]</p>

![Scatter Sepal Code](/images/scatterSepal.JPG)

<p>Looking at the scatter plots we can make some observations about the data</p>

![Scatter Speal](/res/scatterSepal.jpg)

<p>Iris-Setosa appears to be the only flower that differs in a distinctive way in terms of speal length and width. However Iris-versicolor and Iris-virginica appear a little more varied and mixed together</p>

<p>Next we will look at the relationship between petal length and width. Coding this was much the same processs as the previous graph.</p>

![Scatter Petal](/images/scatterPetal.JPG)

<p>So looking at the relationship between petal length and width we can make some observations.</p>

![Petal Plot](/res/scatterPetal.jpg)

<p>Examining the graph tells us that these two measurements increase together. Logically that must be true if they did not they would be very long thin petals, or else very short and wide petals. The graph also shows that this is a very good way to differinate between the different flowers</p>

## Machine Learning

<p>From what we have learned thus far about our data, this dataset has shown to be a good candidate for machine learning. In this section I will attempt to do some machine learning on this dataset. I will look at two algorithims to make predictions; Decision trees and K-means clustering. This is my first attempt at using this software so I won't be delving too much into the specifics of each algorithim. I have relied solely on online tutorials and doumentation for this portion of the project [16, 17, 18, 22] </p>

<p>The first step in machine learning is to split the code into 2 parts. The first is for training the algorithinm and the other is for testing to see how accurate it is.[22] </p>

![Split Data Code](/images/splitData.JPG)

<p>We can also see how the data is actually split aswell:</p>

![How data is split](/images/splitDataBreakdown.JPG)

<p>We want the algorithim to learn how to pick out patterns in the data. But in the real world we want it to look at all species of Iris not just the ones in this particular dataset. There could be patterns among the 150 specimens that are specific to this dataset, that may not apply to all species of Iris. This is part of the reason why we split up the data. This also allows us to test the accuracy of the algorithim, which is very important as it is a big factor when choosing which algorithim to use.[16]</p>

<p>So the first algorithim we are going to look at is decision trees. In the simplest terms a decision tree generates rules on how to classify the data. It has different paths to follow depending on if certain conditions are true or false.[18]</p>

![Decision Tree Code](/images/decisionTree.JPG)

<p>Next we can use the graphviz application to visualise the tree.[20, 21]</p>

![View Tree](/images/viewDecision.JPG)

<p>Then we can actually have a look at the decision tree generated: </p>

![Decision Tree1](/images/tree1.JPG)
![Decision Tree1](/images/tree2.JPG)

<p>So as you can see the program will work its way down through the trees until it reaches a classification for each flower. For example you can see the easiest flower to classify is the setosa (which we knew from our earlier investigation!). Following the tree if the petal length is <= 2.5cm then it is a setosa, if not it will move to the next branch and so on until it is classified. </p>

<p>Next we want to look at the accuracy of the algorithim.[17, 18]</p>

![Tree Accuracy](/images/accuracyTree.JPG)

![Tree Result](/images/scoreTree.JPG)

<p>The decision tree algorithim has 93% accuracy which is quite good. But there are still going to be some errors. Lets take a look at k-NN clustering to see if that is more accurate.</p>

<p>kNN clustering (where NN stands for nearest neighbours) will generate groups of clusters that will be sorted based on the data available to the algorithim.[22] Our clusters will be based on species which should work quite well based on the graphs we examined above.</p> 

![Splitting the data](/images/trainSet.JPG)

<p>kNN will use the training data to set the clusters, and it uses the data from the training to decide on where the test data will be sorted [16, 18, 22]</p>

![kNN Code](/images/knnCode.JPG)

<p>This code will generate a table of predictions based on our test data so we can actually see how the algorithim is sorting the data</p>

![kNN table](/images/knnTable.JPG)

<p>So this algorithim is more accurate than the previous with accuracy of 97%. The only time if failed according to the table (last entry in table) was between a versicolor and virginica which as we had seen from the scatterplots earlier overlapped on some of these features. So clearly the algorithim will fail if the features are very close together.</p>

## Conclusion
<p>From a simple data set we can learn so much about these flowers! Not only did we learn about trends and patterns as shown by the earlier exploration of the data such as summarising the general stastical data and the various graphs and plots generated. But also the real world application of machine learning and how this dataset could be used to predict the species of other flowers based solely on their petal and sepal measurements. Looking at the two algorithims they only failed when the specimens were too close to each other. But the majority of the time they were correctly able to identify the species. It just shows how powerful these tools can be when working with datasets.</p>

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
23. [Scikit-learn estimator object](https://scikit-learn.org/stable/tutorial/statistical_inference/settings.html)