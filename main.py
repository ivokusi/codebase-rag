from utils import clone_repository, embed_documents, get_main_files_content, perform_rag


from dotenv import load_dotenv
from pinecone import Pinecone
from openai import OpenAI
import streamlit as st
import requests
import json
import os

# repo_url = "https://github.com/CoderAgent/SecureAgent"

# path = clone_repository(repo_url)
# file_content = get_main_files_content(path)

# embed_documents(file_content, "codebase-rag", repo_url)

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=PINECONE_API_KEY)
pinecone_index = pc.Index("codebase-rag")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY
)

st.title("Codebase Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Message Codebase Bot"):
    
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = perform_rag(prompt, pinecone_index, client)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})