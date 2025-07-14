from db.initialize_store import get_vector_store

def view_docs():
    store = get_vector_store()
    return store.get(include=['embeddings', 'documents', 'metadatas'])