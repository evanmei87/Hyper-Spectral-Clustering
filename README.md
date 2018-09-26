# Hyper-Spectral-Clustering

Clustering-based analysis approach to hyper-spectral image cubes. So far, this code can subdivide the cube into like groups based on a distance calculation between all of it's dimensions.

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

The number between the two underscores are all we really care about because that's how the code will organize this file directory to match the header with its raw file. There can not be more than two files with that specific number and both files can not have the same file extension. 

### Deployment
From here we can run the code and it will automatically analyze all hyperspectral cubes in that raw file folder. Then an output text file will be returned with the 2d pixel coordinates and it's cluster number. We can visualize this output using a program like imageJ and clicking File -> import -> Text Image. 

## Author
* **Evan Mei**
