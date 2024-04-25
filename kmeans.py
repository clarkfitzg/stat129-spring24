from collections import Counter
import random

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans


good = "good happy joy fun sweet wonderful positive great".split()
bad = "bad terrible awful misery pain".split()

def gendoc(words, n=10):
    """ 
    Generate a string containing n elements from words,
    possibly repeated.
    """
    weights = np.linspace(1, 0.3, num=len(words))
    probs = weights / weights.sum()
    w = np.random.choice(words, n, p = probs)
    return " ".join(w)

ngood = 15
nbad = 10
good = [gendoc(good, 5) for x in range(ngood)]
bad = [gendoc(bad, 5) for x in range(nbad)]

# 1 in between, just for fun :)
corpus = np.array(good + bad + ["good bad happy terrible"])
np.random.shuffle(corpus)


tf = TfidfVectorizer()

X = tf.fit_transform(corpus)
X.shape

terms = tf.get_feature_names_out()

# Principal Components using SVD
############################################################

# Experiment with this
ndim = 5 
svd = TruncatedSVD(n_components=ndim, random_state=230)
svd.fit(X)

# These are the principal components
Xpc = svd.transform(X)

X.shape

Xpc.shape

# Percentage of total variance in data explained by 
# these principal components
100 * sum(svd.explained_variance_ratio_)


# Kmeans!
############################################################
# Experiment with different values
K = 2

km = KMeans(n_clusters=K, random_state=2408)
# We can also just use X here if we like
clusters = km.fit_predict(Xpc)

# How many are in each cluster?
Counter(clusters)

# What are the centers?
Xcenters = svd.inverse_transform(km.cluster_centers_)
# Do this if we're not using the Principal components
#Xcenters = km.cluster_centers_

# An index of which terms have the largest coefficients
# in each cluster
bigindex = np.argsort(Xcenters)
for i in range(K):
    # The 3 most important terms in each cluster
    print(terms[bigindex[i, :]][-3:])

# Let's look at 4 random documents from cluster 1
g = clusters == 1
gdocs = corpus[g]
np.random.choice(gdocs, size=4, replace=True)
