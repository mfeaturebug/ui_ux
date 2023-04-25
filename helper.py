import streamlit as st
import pandas as pd
import numpy as np
import openai
from openai.embeddings_utils import get_embedding, cosine_similarity


def get_embeddings_data_frame():
    embeddings_path = "./embeddings/ui_ux_embeddings.csv"
    df = pd.read_csv(embeddings_path)
    df["embedding"] = df.embedding.apply(eval).apply(np.array)
    return df


# search through the reviews for a specific product
def search_book_context(df, query, n=3):
    try:
        # query_embedding = get_embedding(query, engine="text-embedding-ada-002")
        query_embedding = openai.Embedding.create(
            model='text-embedding-ada-002',
            input=query,
        )["data"][0]["embedding"]
        df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, query_embedding))
        results = (
            df.sort_values("similarity", ascending=False)
            .head(n)
        )
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        results = 'Something went wrong'
    return results


def get_gpt_response(context, query):
    context = context.iloc[0]
    prefix = 'Use the below text to answer the subsequent question in under 10 sentences. If the answer cannot be found in the text, write "I could not find an answer."'
    prefix = prefix +'\n\nText: ' + context['text']
    question = "\n\n Question: " + query
    prompt = prefix + question
    response = {
        'chunk': context['file_name'],
        'similarity': context['similarity'],
        'file_path': context['file_path']
    }
    # print(prompt)
    try:
        response['gpt_full_response'] = openai.Completion.create(
            engine="text-davinci-003",
            # engine='text-curie-001',
            prompt=prompt,
            temperature=0.6,
            max_tokens=200,
        )
    except Exception:
        response['gpt_full_response'] = 'Something seems to have gone wrong. I am at my wits end!!'
    return response
