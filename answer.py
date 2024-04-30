from google.cloud import aiplatform
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_google_vertexai import (
    VectorSearchVectorStore,
)
from langchain_google_vertexai import VertexAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
llm = VertexAI(model_name="gemini-pro")

project_id="<Enter GCP project id>"
region="<Enter region>"
gcs_bucket_name="<Enter Bucket name>"
index_id="<Enter index id>"
endpoint_id="<Enter endpoint id>"

embedding_model = VertexAIEmbeddings(model_name="textembedding-gecko@003")

vector_store = VectorSearchVectorStore.from_components(
    project_id=project_id,
    region=region,
    gcs_bucket_name=gcs_bucket_name,
    index_id=index_id,
    endpoint_id=endpoint_id,
    embedding=embedding_model,
)


retriever = vector_store.as_retriever()

retrieval_qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
)

question = "Where did Akhil Reddy graduated?"
response = retrieval_qa({"query": question})
print(f"{response['result']}")