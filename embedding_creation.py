from google.cloud import aiplatform
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_google_vertexai import (
    VectorSearchVectorStore,
)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


project_id="<Enter GCP project id>"
region="<Enter region>"
gcs_bucket_name="<Enter Bucket name>"
index_id="<Enter index id>"
endpoint_id="<Enter endpoint id>"

embedding_model = VertexAIEmbeddings(model_name="textembedding-gecko@003")

loader = PyPDFLoader("<Enter file location>")
pages = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)
doc_splits = text_splitter.split_documents(pages)


texts = [doc.page_content for doc in doc_splits]
metadatas = [doc.metadata for doc in doc_splits]


vector_store = VectorSearchVectorStore.from_components(
    project_id=project_id,
    region=region,
    gcs_bucket_name=gcs_bucket_name,
    index_id=index_id,
    endpoint_id=endpoint_id,
    embedding=embedding_model,
)

vector_store.add_texts(texts=texts, metadatas=metadatas, is_complete_overwrite=True)