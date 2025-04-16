import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.metrics import silhouette_score
import re
import folium
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')



dataset = "path"


# Step 0: Load your dataset (since you're not using Power BI)
# Replace 'tickets.csv' with the path to your actual data file
try:
    dataset = pd.read_csv(dataset)
except FileNotFoundError:
    print(f"Error: The file '{dataset}' was not found. Please provide the correct path to your data file.")
    exit(1)
    
dataset = dataset[
    (dataset['resolved_by_name'] != 'specificName') &
    (dataset['assignee_name'] != 'specificName')
]

# Print the column names to debug
print("Dataset columns:", dataset.columns.tolist())

# Step 1: Dataset Preprocessing
def preprocess_text(text):
    """
    Preprocess ticket descriptions: lowercase, remove punctuation, tokenize, remove stopwords.
    """
    # Handle non-string input (e.g., NaN or numbers)
    if not isinstance(text, str):
        text = ''
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords (English and French)
    stop_words = set(stopwords.words('english')).union(set(stopwords.words('french')))
    
    custom_stopwords = {'bonjour','complete', 'please','fare','find', 'fine','cognos'
                        , 'already','description','provide', 'new', 'essayé', 'related'
                        , 'être', 'mandatory','fait','faire', 'suite','extrêmement,','fais','365'}
    stop_words.update(custom_stopwords)
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Handle NaN values in the description column
# Dynamically find the description column
description_column = None
for col in dataset.columns:
    if 'description' in col.lower():
        description_column = col
        break

if description_column is None:
    raise ValueError("No column containing 'description' found in the dataset. Available columns: " + str(dataset.columns.tolist()))

dataset[description_column] = dataset[description_column].fillna('')  # Replace NaN with empty string

# Apply preprocessing to ticket descriptions
dataset['cleaned_descriptions'] = dataset[description_column].apply(preprocess_text)

# Step 2: Feature Extraction with TF-IDF
vectorizer = TfidfVectorizer(max_features=1000, min_df=2, max_df=0.8)
tfidf_matrix = vectorizer.fit_transform(dataset['cleaned_descriptions'])

# Try different cluster counts
for k in range(3, 9):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    labels = kmeans.fit_predict(tfidf_matrix)
    score = silhouette_score(tfidf_matrix, labels)
    print(f"Silhouette Score for k={k}: {score:.4f}")

# Step 3: Applying K-Means Clustering
num_clusters = 9  # Adjust as needed
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init='auto')  # Modern scikit-learn parameter
dataset['cluster'] = kmeans.fit_predict(tfidf_matrix)


# Step 4: Extract and Save Top Terms per Cluster
def get_top_terms_per_cluster(vectorizer, tfidf_matrix, kmeans, n_terms=10):
    """
    Extract top TF-IDF terms for each cluster and return as a DataFrame.
    """
    terms = vectorizer.get_feature_names_out()
    order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
    
    top_terms_data = []
    for i in range(kmeans.n_clusters):
        top_terms = [terms[ind] for ind in order_centroids[i, :n_terms]]
        top_scores = [kmeans.cluster_centers_[i, ind] for ind in order_centroids[i, :n_terms]]
        
        # Print for reference
        print(f"\nCluster {i}:")
        print("Top terms:", top_terms)
        
        # Collect data for the DataFrame
        for rank, (term, score) in enumerate(zip(top_terms, top_scores), 1):
            top_terms_data.append({
                'Cluster': f'Cluster {i}',
                'Rank': rank,
                'Term': term,
                'Score': round(score, 4)
            })
    
    return pd.DataFrame(top_terms_data)

# Save top terms to CSV
top_terms_df = get_top_terms_per_cluster(vectorizer, tfidf_matrix, kmeans, n_terms=10)
top_terms_df.to_csv("top_terms_per_cluster.csv", index=False)
print("Top terms saved to 'top_terms_per_cluster.csv'")

# Step 5: Save Ticket Cluster Assignments
# Save the dataset with cluster assignments (include relevant columns like id, description, cluster)
if 'id' not in dataset.columns:
    dataset['id'] = range(1, len(dataset) + 1)  # Add an ID column if not present
dataset_to_save = dataset[['number', description_column, 'cluster']].copy()
dataset_to_save.rename(columns={description_column: 'description'}, inplace=True)
dataset_to_save.to_csv("ticket_clusters.csv", index=False)
print("Ticket cluster assignments saved to 'ticket_clusters.csv'")

# Step 6: Visualizing Clusters on a Map with Folium (if applicable)
try:
    import folium
    from folium.plugins import MarkerCluster
    
    if 'latitude' in dataset.columns and 'longitude' in dataset.columns:
        # Create a Folium map centered on the mean coordinates
        map_center = [dataset['latitude'].mean(), dataset['longitude'].mean()]
        folium_map = folium.Map(location=map_center, zoom_start=10)

        # Add marker clusters
        marker_cluster = MarkerCluster().add_to(folium_map)

        # Color-code clusters
        colors = ['red', 'blue', 'green', 'purple', 'orange']  # Adjust based on num_clusters
        for idx, row in dataset.iterrows():
            cluster_id = row['cluster']
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=5,
                color=colors[cluster_id % len(colors)],
                fill=True,
                fill_color=colors[cluster_id % len(colors)],
                fill_opacity=0.7,
                popup=f"Cluster {cluster_id}: {row[description_column][:50]}..."
            ).add_to(marker_cluster)

        # Save the map to an HTML file
        folium_map.save('ticket_clusters_map.html')
        print("Map saved as 'ticket_clusters_map.html'. Open it in a browser to view.")
    else:
        print("No latitude/longitude data found. Skipping map visualization.")
except ImportError:
    print("Folium not installed. Skipping map visualization.")

# Step 7: Visualize Clusters in 2D using PCA
# Reduce TF-IDF matrix to 2D using PCA
pca = PCA(n_components=2)
tfidf_2d = pca.fit_transform(tfidf_matrix.toarray())

from collections import Counter




# Transform the dictionary into a DataFrame for export
cluster_data = []

# Loop through the DataFrame rows
for _, row in top_terms_df.iterrows():
    cluster_data.append({
        'cluster': row['Cluster'],     # Cluster name, e.g., 'Cluster 0'
        'word': row['Term'],           # Term from that cluster
        'score': row['Score'],         # TF-IDF score
        'rank': row['Rank']            # Rank of the word in the cluster
    })



# Bar graphic: Cluster vs. most frequent words
# Convert the list of dictionaries into a DataFrame
df_cluster_words = pd.DataFrame(cluster_data)

# Export the DataFrame to a CSV file
df_cluster_words.to_csv('top_words_by_cluster.csv', index=False)

import seaborn as sns
import matplotlib.pyplot as plt

# Plotting top terms by cluster
plt.figure(figsize=(12, 6))
sns.barplot(data=top_terms_df, x='Cluster', y='Score', hue='Term')
plt.title("Top Terms per Cluster")
plt.ylabel("TF-IDF Score")
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

print("")

#------------------------------
#Create categories to anlise effort
#------------------------------

from collections import defaultdict

# Get top terms per cluster from your previous function
top_terms_df = get_top_terms_per_cluster(vectorizer, tfidf_matrix, kmeans, n_terms=10)

# Step 1: Aggregate top terms by cluster
terms_by_cluster = defaultdict(list)

for _, row in top_terms_df.iterrows():
    cluster_id = int(row['Cluster'].replace('Cluster ', ''))
    terms_by_cluster[cluster_id].append(row['Term'])

# Step 2: Build a dataframe to assign manual or suggested categories
cluster_category_rows = []

# Suggest categories manually based on terms OR automate below
for cluster_id, terms in terms_by_cluster.items():
    suggested_category = ''
    
    if any(word in terms for word in ['error', 'fail', 'bug', 'crash', 'restart']):
        suggested_category = 'Error/Failure'
    elif any(word in terms for word in ['power bi', 'dashboard', 'report', 'workspace']):
        suggested_category = 'PowerBI/Reports'
    elif any(word in terms for word in ['ax', 'dynamix', 'reset']):
        suggested_category = 'AX'
    elif any(word in terms for word in ['oasis']):
        suggested_category = 'Oasis'
    elif any(word in terms for word in ['login', 'printer', 'lumenlabel','label']):
        suggested_category = 'Lumenlabel'
    else:
        suggested_category = 'Other'

    cluster_category_rows.append({
        'cluster': cluster_id,
        'top_terms': ', '.join(terms),
        'suggested_category': suggested_category
    })

# Step 3: Create a dataframe and export
df_cluster_categories = pd.DataFrame(cluster_category_rows)
df_cluster_categories.to_csv('cluster_categories.csv', index=False)
print("Suggested categories saved to 'cluster_categories.csv'")




#------------------------------------------------------
# STEP 1: Define Categories of Issues
#-----------------------------------------------------

# Optional: Map cluster numbers to human-readable categories
cluster_labels = {
    0: "Access Issues",
    1: "AX Dynamix Failures", 
    2: "LumenLabel",
    3: "Software Installation",
    4: "Oasis"
}

#STEP 2: Estimate Time Spent per Ticket
# Add estimated resolution time (hours)
time_estimates = {
    "Access Issues": 0.41,
    "AX Dynamix Failures": 1.13,
    "LumenLabel": 1.42,
    "Software Installation": 11.27,
    "Oasis": 4.89
}

# Map values into dataset
dataset['issue_category'] = dataset['cluster'].map(cluster_labels)
dataset['estimated_hours'] = dataset['issue_category'].map(time_estimates)

# Convert date if you have a timestamp column
if 'created_date' in dataset.columns:
    dataset['month'] = pd.to_datetime(dataset['created_date']).dt.to_period('M').astype(str)
else:
    dataset['month'] = "Unknown"

# Columns to export
columns_to_export = ['number', 'cleaned_descriptions', 'issue_category', 'estimated_hours', 'cluster', 'month']
dataset[columns_to_export].to_csv("powerbi_ticket_clusters.csv", index=False)

columns_to_export = [
    'number', 
    'cleaned_descriptions', 
    'issue_category', 
    'estimated_hours', 
    'cluster', 
    'month',
    'resolved_by_name',
    'assignee_name'
]

dataset[columns_to_export].to_csv("powerbi_ticket_clusters_with_people.csv", index=False)
