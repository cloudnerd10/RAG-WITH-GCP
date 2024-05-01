RAG with GCP: Leveraging Vector Search and LLMs
This repository provides a framework for building Retrieval Augmented Generation (RAG) solutions using Google Cloud Platform (GCP) native services, including vector search and large language models (LLMs), in conjunction with LangChain.

Files and Workflow
index_creation.py: This script sets up the vector search index and deploys the index endpoint along with a storage bucket. Run this first to establish the foundational infrastructure.
embedding_creation.py: This script generates embeddings for your files and updates them in the vector search database. Execute this after creating the index.
answer.py: With the index and embeddings in place, use this script to ask questions and retrieve answers from your files.
Getting Started
Run index_creation.py: This will create the necessary vector search index and deploy the endpoint along with a storage bucket.
Run embedding_creation.py: This will process your files and update the vector search database with the generated embeddings.
Run answer.py: Start asking questions and explore the RAG capabilities powered by GCP and LangChain.
Note: Ensure you have the required GCP services and LangChain set up before running the scripts.
