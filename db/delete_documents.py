from db.initialize_store import get_vector_store

def delete_docs():
    store = get_vector_store()
    store.delete(ids=['ID1', 'ID7'])