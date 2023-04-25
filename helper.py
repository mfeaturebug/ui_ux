import streamlit as st
import pandas as pd
import numpy as np

EMBEDDING_MODEL = "text-embedding-ada-002"


def get_embeddings_data_frame():
    embeddings_path = "./embeddings/ui_ux_embeddings.csv"
    df = pd.read_csv(embeddings_path)
    df["embedding"] = df.embedding.apply(eval).apply(np.array)
    return df

