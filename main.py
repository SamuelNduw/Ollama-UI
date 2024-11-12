import streamlit as st
import requests
import json
from models import get_local_models

OLLAMA_API_URL = "http://localhost:11434/api/generate"  

def ollama_chat_stream(query, model="llama3.2:1b"): 
    payload = {
        "model": model,
        "prompt": query,
        "stream": True 
    }
    
    try:
        with requests.post(OLLAMA_API_URL, json=payload, stream=True) as response:
            response.raise_for_status() 
            # Ensure content is decoded into string
            for chunk in response.iter_content(chunk_size=None):
                if isinstance(chunk, bytes):  # Check if the chunk is bytes and decode
                    chunk = chunk.decode('utf-8')
                # Parse the chunk as JSON and yield only the 'response' field
                try:
                    chunk_json = json.loads(chunk)
                    if 'response' in chunk_json:
                        yield chunk_json['response']  # Yield only the 'response' field
                except json.JSONDecodeError:
                    continue  # Skip if chunk is not complete JSON
    except requests.exceptions.RequestException as e:
        yield f"An error occurred: {e}"

# Streamlit UI
st.title(" Sam's Ollama-Powered Chatbot")

select_model = st.sidebar.selectbox("Select Model",
                                    get_local_models(), index=0)

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box for user query
user_input = st.chat_input("Ask a question:")

# When the user submits a query
if user_input:
    # Append user message to session state and display it
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Display the bot response while streaming
    bot_response = f"Model:  {select_model} => "
    with st.chat_message("assistant"):
        bot_message_placeholder = st.empty()  # Placeholder to update message progressively
        # Stream response from Ollama
        for chunk in ollama_chat_stream(user_input, model=select_model):
            bot_response += chunk
            bot_message_placeholder.markdown(bot_response)  # Update message in real-time
    
    # Append bot response to session state
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
