from google.cloud import aiplatform
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_google_vertexai import (
    VectorSearchVectorStore,
)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google.cloud import storage

PROJECT_ID = "<Enter Your GCP project id>"
LOCATION = "<Enter Region>"
BUCKET = "<Enter bucker name>"
BUCKET_URI = f"gs://{BUCKET}"
DIMENSIONS = 768
DISPLAY_NAME = "<Enter index name>"

storage_client = storage.Client()
bucket = storage_client.create_bucket(BUCKET,location=LOCATION)

my_index = aiplatform.MatchingEngineIndex.create_tree_ah_index(
    display_name=DISPLAY_NAME,
    dimensions=DIMENSIONS,
    approximate_neighbors_count=150,
    distance_measure_type="DOT_PRODUCT_DISTANCE",
    index_update_method="STREAM_UPDATE",  # allowed values BATCH_UPDATE , STREAM_UPDATE
)


my_index_endpoint = aiplatform.MatchingEngineIndexEndpoint.create(
    display_name=f"{DISPLAY_NAME}-endpoint", public_endpoint_enabled=True
)


my_index_endpoint = my_index_endpoint.deploy_index(
    index=my_index, deployed_index_id=DISPLAY_NAME
)

my_index_endpoint.deployed_indexes