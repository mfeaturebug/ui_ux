import streamlit as st
import pandas as pd
from query_test import ask
import openai

EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"

st.title("Everything about becoming a UI UX Expert!")
# st.sidebar.header("Instructions")
# st.sidebar.info(
#     '''Ask anything about being a UI UX Designer!.
#        '''
# )

# Set the model engine and your OpenAI API key
model_engine = "text-curie-001"


def main():
    '''
    This function gets the user input, pass it to ChatGPT function and
    displays the response
    '''
    # Get user input
    user_query = st.text_input("Who is a UX designer?")

    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        response = ask(user_query)
        return st.write(f"{user_query} {response}")


# call the main function
main()
