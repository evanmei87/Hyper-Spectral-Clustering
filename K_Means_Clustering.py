
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


class K_Means:
    def __init__(self, k=25, tol=.001, max_width = 200, max_iter = 300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter
        self.max_width = max_width
    def fit(self, data):
        self.centroids = {}
        
        for i in range(self.k):
            indices = np.random.randint(self.max_width, size = self.k)
            self.centroids[i] = data[indices[0]][indices[1]]
        
        for i in range(self.max_iter):
            self.classifications = {} #cluster number, array of data points
            self.cluster_cords = {}
            
            for i in range(self.k):
                self.classifications[i] = []
                self.cluster_cords[i] = []
                
            #for featureset in data:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    featureset = data[i][j]
                    distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]

                    #calculate two distances from point to each centroid
                    #distances size is equal to k
                    classification = distances.index(min(distances)) #index of the lowest dist
                    self.classifications[classification].append(featureset) #puts the lower dist into that centroid dict
                    
                    cord = [i, j] #row X column
                    self.cluster_cords[classification].append(cord)
                    
            prev_centroids = dict(self.classifications)
            
            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis =0)
                #take average of all points in the centroid dictionary
            optimized = True
            for c in self.centroids:
                original_centroid = prev_centroids[c] #compare previous centroid
                current_centroid = self.centroids[c]
                #print(original_centroid)
                if np.linalg.norm(current_centroid - original_centroid) >10:    
                    #checks whether the centroids are optimized thus we can save runtime
                    optimized = False
            if optimized:
                break
                
    def predict(self,data):
        distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification

