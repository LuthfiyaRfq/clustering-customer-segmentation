import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder

def scatter_pca(new_data_df):
  sample_data_df = pd.read_csv('assets/subset.csv')
  combined_df = pd.concat([sample_data_df[['Partner', 'Education_Level']], new_data_df[['Partner', 'Education_Level']]], ignore_index=True)

  label_encoder = LabelEncoder()
  label_encoder.fit(combined_df['Partner'])
  sample_data_df['Partner'] = label_encoder.transform(sample_data_df['Partner'])
  new_data_df['Partner'] = label_encoder.transform(new_data_df['Partner'])

  label_encoder.fit(combined_df['Education_Level'])
  sample_data_df['Education_Level'] = label_encoder.transform(sample_data_df['Education_Level'])
  new_data_df['Education_Level'] = label_encoder.transform(new_data_df['Education_Level'])

  pca_input_df = pd.concat([sample_data_df[['Income', 'Kidhome', 'Teenhome', 'Age', 'Partner', 'Education_Level']], 
                          new_data_df[['Income', 'Kidhome', 'Teenhome', 'Age', 'Partner', 'Education_Level']]], 
                          ignore_index=True)

  pca = PCA(n_components=2)
  pca_result = pca.fit_transform(pca_input_df)

  sample_pca_result = pca_result[:len(sample_data_df)]
  new_data_pca_result = pca_result[len(sample_data_df):]

  plt.figure(figsize=(8, 6))

  # Plot each cluster separately to add to legend
  for cluster in sample_data_df['Clusters'].unique():
      cluster_data = sample_pca_result[sample_data_df['Clusters'] == cluster]
      plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f'Cluster {cluster}', s=100)

  # Plot new data
  plt.scatter(new_data_pca_result[:, 0], new_data_pca_result[:, 1], c='black', label='Data prediction', s=100, marker='x')

  plt.title("Customer Segmentation Clustering Visualization")
  plt.xlabel("PCA Component 1")
  plt.ylabel("PCA Component 2")
  plt.legend()
  plt.grid(True)

  st.pyplot(plt)