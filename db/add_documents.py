from db.initialize_store import get_vector_store
from data.documents import get_cwc_documents

def add_docs():
    store = get_vector_store()
    docs = get_cwc_documents()
    store.add_documents(docs)