#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:43:20 2024

@author: wesleychapman
HW 4
"""

import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np





# define url and parameters
api_url = "https://newsapi.org/v2/everything"
params = {"q" : "minnesota twins",
          "apiKey" : "6f14aaa536ff410dbb27b7e688f9cd51"}

# get data from api
response = requests.get(api_url, params = params)
data = response.json()

# drop blank articles
articles = []
for article in data['articles']:
    if article['content']:
        articles.append(article['content'])
        
# set up vectorizer
vectorizer = TfidfVectorizer(max_features=200)

# transform articles into TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(articles).toarray()

# set up PCA
pca = PCA(n_components=2)

# apply PCA
pca_data = pca.fit_transform(tfidf_matrix)

# find kmeans
cluster = KMeans(n_clusters=3, random_state=14, n_init=10)

# fit kmeans to data
cluster = cluster.fit(pca_data)

# access cluster labels
clusters = cluster.labels_

# plot pca data
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=clusters, cmap='viridis')
plt.title("KMeans Clustering of Articles")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()
plt.show()
    

    
def main():  
    
    ## QUESTIONS:
        
    # Q1: What keyword(s) did you use in your query?
    keyword = params['q']
    print(f'Q1: The keywords I used are "{keyword}."')
    
    
    # Q2: After PCA has been applied, if number of components is 2, 
    #     what are the two values of the first article in your dataset?
    print(f'Q2: The first two values of the first article in\
          my dataset are {pca_data[0]}.')
    
    
    # Q3: What value of k is optimal based on inertia?
    # find inertia values
    inertia = []
    for i in np.arange(1, 9):
        test = (KMeans(n_clusters=i, random_state=14, n_init=10))
        test.fit(pca_data)
        inertia.append(test.inertia_)
    print('Q3: Check plot for elbow value.')
    
    # plot to determine optimal k 
    plt.plot(np.arange(1, 9), inertia, c='red', marker='o', markersize=4)
    plt.xlabel('k')
    plt.ylabel('Inertia')
    plt.title('k Clusters vs Inertia Value')
    
    
    # Q4: Once k has been optimized, how many articles are in each cluster?
    cluster0_total = 0
    cluster1_total = 0
    cluster2_total = 0
    for i in clusters:
        if i == 0:
            cluster0_total += 1
        elif i == 1:
            cluster1_total += 1
        elif i == 2:
            cluster2_total += 1
    print(f'Q4: Total articles per cluster: \
          Cluster 0: {cluster0_total}\
          Cluster 1: {cluster1_total}\
              Cluster 2: {cluster2_total}')
  
    
    
if __name__ == "__main__":
    main()














