# Hyper-Spectral-Clustering

Clustering-based analysis approach to hyper-spectral image cubes. This code can subdivide the cube into groups that we determine to be the most similar based on a distance calculation between all of it's dimensions.

## Getting Started

Hopefully these instructions will allow you to run a copy of this code on your local machine. 

### Prerequisites 

First, I would recommend that you use [Anaconda] (https://www.anaconda.com/download/). Which in my opinion will make it much easier to download all the packages I used. Download the Python 3.6 version. Then open Anaconda Navigator. By default Jupyter Notebook should be available for installation. Install Jupyter Notebook.

![](https://github.com/evanmei87/Hyper-Spectral-Clustering/blob/master/ReadMeImages/jupyter%20notebook.JPG)

I used ImageJ to visualize the color segmented output. You may find it helpful when you want to look at where the groups formed.
### Packages

Under the Enviroments tab, we need to install the following packages:
```
numpy
matplotlib
```
From that point, we are ok to run the code.

### Raw File Folder
There is a folder in this repository called
```
Raw_Data_with_hdr
```

This is where we need to put our raw hyperspectral cubes and their accompanying header files. The code will run on all the files listed in the directory. Generally the files all need to have the following pattern ie
```
Raw_someNumber_someLocation.raw
Raw_someNumber_someLocation.hdr
```
Here is an example:
![](https://github.com/evanmei87/Hyper-Spectral-Clustering/blob/master/ReadMeImages/files.JPG)

The number between the two underscores is all we really care about because that's how the code will organize this file directory to match the header with its raw file. There can not be more than two files with that specific number and both files can not have the same file extension. 

### Deployment
From here we can run the code and it will automatically analyze all hyperspectral cubes in that raw file folder. Currently, the default number of clusters that will be created is 2, but we can change this by changing the k value in this line of code at the end of the CleanedHyperClustering notebook. Additionally change max_iter to increase the accuracy of the clustering but at the cost of extra runtime.

```
clf = clusterMod.K_Means(k = 2, max_width = min(length, width), max_iter = 10)
```

So far in my tests, 25 clusters yields a decent distribution of groups while also not taking an entire day to analyze. Typical runtime for 25 clusters is around 3 hours. 200-300 iterations yields more defined groups.

To run the code, launch Jupyter Notebook and navigate to where you downloaded this repository and open CleanedHyperClustering. From there we can click Kernel -> Restart and Run All.

An output text file with the name output(fileNumber).txt will be created with the 2d pixel coordinates and it's cluster number. We can visualize this output using a program like imageJ and clicking File -> import -> Text Image. 

### Future Updates
Some time in the future I would like to classify these clusters with groundtruth to determine how accurate the clustering is. When compared to the NDVI approach of finding vegetation, this clustering approach was successfully able to identify the vegetation and put all those coordinates into one group. Here is an output image of a 25-group cluster where I highlighted the one group that identified vegetation.

![](https://github.com/evanmei87/Hyper-Spectral-Clustering/blob/master/ReadMeImages/ndvi%20comparison.JPG)

This method also has the advantage over the NDVI method because we are analyzing more than just two values of each point. So potentially we can identify diseases, hydration, sunlight, etc. using clustering. There are already some interesting looking groups that have been clustered so far in the data I have examined.

Once we classify with the groundtruth we would ideally have enough data to create a 2-layer neural net that can classify without the groundtruth and we then can identify and label the clusters automatically.
## Author
* **Evan Mei**
