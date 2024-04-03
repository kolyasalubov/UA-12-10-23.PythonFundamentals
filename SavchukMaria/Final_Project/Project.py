# -*- coding: utf-8 -*-

"""Копія записника "Doctor Segmentation.ipynb"
""" 
"Doctor Segmentation.ipynb"

Automatically generated by Colaboratory.

Original file is located at
https://colab.research.google.com/drive/1aT3rBzDOEuOgn1YZ9uyb3ewiolSQjAXi#scrollTo=q9ApdSVsEmaS

The goal of this project is to group  HCPs into specific groups so that the
marketing team can target them with products and services tailored to that specific groups.


---
I will use k-means clustering method.

K-Means clustering algorithm is an unsupervised algorithm and it is used to segment the interest area from the background. It clusters, or partitions the given data into K-clusters or parts based on the K-centroids.

The algorithm is used when you have unlabeled data(i.e. data without defined categories or groups). The goal is to find certain groups based on some kind of similarity in the data with the number of groups represented by K.

# Healthcare Professional Segmentation Project
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/content/Doctors.csv')
data.head()

data.dtypes

data.describe ()

data.info()

"""### DATA ANALYSIS


"""

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(16, 5))

plt.subplot(1, 3, 1)
sns.histplot(data['Speciality'])
plt.title("Distribution of Speciality")
plt.xlabel("Range of Speciality")
plt.ylabel("Count")

plt.subplot(1, 3, 2)
sns.histplot(data['PatientNumbers'])
plt.title("Distribution of PatientNumbers")
plt.xlabel("Range of PatientNumber")
plt.ylabel("Count")

plt.subplot(1, 3, 3)
sns.histplot(data['Prescription'])
plt.title("Distribution of Prescription")
plt.xlabel("Range of Prescription")
plt.ylabel("Count")




plt.show()

sns.pairplot(data)
plt.show()

sns.pairplot(data, vars = ['PatientNumbers',
                          'Prescription'], hue = 'Speciality')

plt.figure(figsize = (16,8))
sns.countplot(data['PatientNumbers'])
plt.title("PatientNumbers")

"""# **K-mean clastering method**

"""

data.columns

x = data.iloc[:, [3,4]].values

x

from sklearn.cluster import KMeans

k = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(x)
    k.append(kmeans.inertia_)

plt.plot(range(1, 11), k)
plt.show()

model = KMeans(n_clusters = 5, init = 'k-means++', random_state = 0)
y_kemsn = model.fit_predict(x)

print(kmeans.cluster_centers_)

plt.figure(1, figsize=(15, 8))

y_kmeans = kmeans.labels_


plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s=100, c='magenta', label='Cluster 1')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s=100, c='cyan', label='Cluster 3')
plt.scatter(x[y_kmeans == 3, 0], x[y_kmeans == 3, 1], s=100, c='green', label='Cluster 4')
plt.scatter(x[y_kmeans == 4, 0], x[y_kmeans == 4, 1], s=100, c='red', label='Cluster 5')


plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='black', label='Centroids')


plt.title('K Means Clustering Algorithm')
plt.xlabel('Number of Patients')
plt.ylabel('Prescription')


plt.legend()


plt.show()

"""**Conclution:**

**Сluster 1** - HCPs with low number patients and prescriptions

**Cluster 2** - HCPs who have lots of patients  and low low presciptions

**Cluster 3** - HCPs who have lots of prescriptions and medium patients

**Cluster 4**- HCPs who have low presciption and medium patients

**Cluster 5** - HCPs with medium presciptions and patients

This analysis will be used by Marketing Team for developing the strategy of working with doctors

"""