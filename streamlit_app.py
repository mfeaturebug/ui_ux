import pandas as pd
from helper import *

EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"

st.title("Everything about becoming a UI UX Expert!")


def main():
    '''
    This function gets the user input, pass it to ChatGPT function and
    displays the response
    '''

    #Get Embeddings dataframe
    @st.cache
    emb = pd.DataFrame()
    emb = get_embeddings_data_frame()
    # Get user input
    user_query = st.text_input("Who is a UX designer?")

    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        response = "High"
        return st.write(f"{user_query} {response}")


# call the main function
main()
