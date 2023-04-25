import pandas as pd
from helper import *

st.title("Everything about becoming a UI UX Expert!")

def main():
    '''
    This function gets the user input, pass it to ChatGPT function and
    displays the response
    '''

    # Get Embeddings dataframe
    # @st.cache_data
    embeddings = get_embeddings_data_frame()

    # Get user input
    user_query = st.text_input("Ask a question about UX Design.", value='Who is a UX Designer?')

    if user_query != ":q" or user_query != "":
        # Pass the query to gpt
        # @st.cache_data
        context = search_book_context(embeddings, user_query, n=1)
        response = get_gpt_response(context, user_query)
        st.write(response['gpt_full_response']['choices'][0]['text'])
        # st.write(response['file_path'])
        return

    # call the main function


main()
