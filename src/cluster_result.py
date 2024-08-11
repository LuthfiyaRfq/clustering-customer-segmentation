import json
import time
import streamlit as st

def __stream_data(text: str):
  for word in text.split(" "):
    yield word + " "
    time.sleep(0.1)

def explanation_result(cluster: int):
  with open('assets/cluster_explanation.json', 'r') as file:
    data = json.load(file)

  cluster_found = False
  for entry in data:
    if entry["Name"] == f"Cluster {cluster}":
      cluster_found = True
      st.header(f"Cluster {cluster}")

      st.subheader("Kesimpulan: ")
      def stream_cluster_info_conclution():
        yield from __stream_data(entry["Kesimpulan"])
      st.write_stream(stream_cluster_info_conclution)

      st.subheader("Strategi Pasar: ")
      def stream_cluster_info_strategy():
        yield from __stream_data(entry["Strategi_pasar"])
      st.write_stream(stream_cluster_info_strategy)
      break

  if not cluster_found:
    st.header(f"Cluster {cluster}")
    def stream_not_found():
      yield "Cluster not found."
    st.write_stream(stream_not_found())