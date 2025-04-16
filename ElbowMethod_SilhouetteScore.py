#------------
# Elbow Method: How to Identify the Ideal Number of Clusters:
#------------
import pandas as pd
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from sklearn.feature_extraction.text import TfidfVectorizer

dataset = pd.read_csv("path")

# Step 1: Dataset Preprocessing
def preprocess_text(text):
    """
    Preprocess ticket descriptions: lowercase, remove punctuation, tokenize, remove stopwords, and stem.
    """
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords (English and French)
    stop_words = set(stopwords.words('english')).union(set(stopwords.words('french')))
    tokens = [word for word in tokens if word not in stop_words]

    return ' '.join(tokens)

# Handle NaN values in the description column
dataset['description'] = dataset['description'].fillna('')  # Replace NaN with empty string

# Apply preprocessing to ticket descriptions
dataset['cleaned_descriptions'] = dataset['description'].apply(preprocess_text)

# Step 2: Feature Extraction with TF-IDF
vectorizer = TfidfVectorizer(max_features=1000,  # Limit features to avoid high dimensionality
                             min_df=2,          # Ignore rare words
                             max_df=0.8)       # Ignore overly common words
tfidf_matrix = vectorizer.fit_transform(dataset['cleaned_descriptions'])


import os
import multiprocessing
os.environ["LOKY_MAX_CPU_COUNT"] = "4"

# Calculando a inércia para diferentes valores de k
inertia = []
k_values = range(1, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit_predict(tfidf_matrix)
    inertia.append(kmeans.inertia_)

# Plotando o Elbow Method
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia, '-o', color='#8d0801')
plt.title('Elbow Method', fontsize=14)
plt.xlabel('Número de Clusters (k)', fontsize=12)
plt.ylabel('Inércia', fontsize=12)
plt.grid()
plt.show()


print("Finish Elbow Method")

#------------
#Silhouette Score: How to Identify the Ideal Number of Clusters:
#------------

from sklearn.metrics import silhouette_score

# Calculando o Silhouette Score para diferentes valores de k
silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(tfidf_matrix)
    score = silhouette_score(tfidf_matrix, kmeans.labels_)
    silhouette_scores.append(score)

# Plotando o Silhouette Score
plt.figure(figsize=(8, 5))
plt.plot(range(2, 11), silhouette_scores, '-o', color='#8d0801')
plt.title('Silhouette Score por Número de Clusters', fontsize=14)
plt.xlabel('Número de Clusters (k)', fontsize=12)
plt.ylabel('Silhouette Score', fontsize=12)
plt.grid()
plt.show()

df_elbow = pd.DataFrame({'k': k_values, 'inercia': inertia})
df_elbow.to_csv("elbow_method.csv", index=False)

from sklearn.cluster import KMeans

def aplicar_kmeans(k):
    kmeans = KMeans(n_clusters=k, random_state=0)
    clusters = kmeans.fit_predict(tfidf_matrix)
    return kmeans, clusters

import numpy as np

def exibir_top_palavras_por_cluster(kmeans_model, tfidf, vectorizer, n_palavras=10):
    termos = vectorizer.get_feature_names_out()
    for i, centro in enumerate(kmeans_model.cluster_centers_):
        top_indices = centro.argsort()[::-1][:n_palavras]
        top_termos = [termos[ind] for ind in top_indices]
        print(f"\n🔹 Cluster {i+1}:")
        print(", ".join(top_termos))

# Supondo que você usou TfidfVectorizer com o nome `vectorizer`
for k in [5, 8, 10]:
    print(f"\n=== Análise para k = {k} ===")
    modelo, _ = aplicar_kmeans(k)
    exibir_top_palavras_por_cluster(modelo, tfidf_matrix, vectorizer)
    
silhouette_scores = [...]
k_values = list(range(2, 11))

df_silhouette = pd.DataFrame({'k': k_values, 'silhouette_score': silhouette_scores})
df_silhouette.to_csv("silhouette_scores.csv", index=False)