from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def get_vector_store():
    return Chroma(
        embedding_function=HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2'),
        persist_directory='chroma_db',
        collection_name='sample'
    )