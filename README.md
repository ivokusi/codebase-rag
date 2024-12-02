# Project Overview

This project, CodebaseBot, is designed to facilitate interaction with codebases using natural language processing (NLP) techniques. It leverages advanced embedding models to understand and retrieve relevant code snippets based on user queries. The main components of the project include:

1. **Repository Cloning**: The project can clone GitHub repositories to a temporary directory, allowing for dynamic analysis of the codebase.

2. **Document Embedding**: It utilizes the Hugging Face embedding models to convert code and documentation into vector representations, enabling efficient similarity searches.

3. **Vector Store Integration**: The project integrates with Pinecone, a vector database, to store and query the embedded documents, ensuring fast retrieval of relevant information.

4. **Chat Interface**: A Streamlit-based web interface allows users to interact with the bot, asking questions about the codebase and receiving contextually relevant answers.

5. **Error Handling**: The code includes robust error handling to manage issues that may arise during repository cloning or file processing.

Overall, CodebaseBot aims to enhance the developer experience by providing an intelligent assistant that can quickly surface relevant code and documentation in response to user inquiries.

# Demo

[CodebaseBot Demo](https://selected-gently-swift.ngrok-free.app/)