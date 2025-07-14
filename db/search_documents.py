from db.initialize_store import get_vector_store

def search_docs(query, k=2):
    store = get_vector_store()
    return store.similarity_search(query=query, k=k)

def search_docs_with_score(query, k=2):
    store = get_vector_store()
    return store.similarity_search_with_score(query=query, k=k)

def search_with_filter():
    store = get_vector_store()
    return store.similarity_search_with_score(
        query="",
        filter={"team": "Real Madrid"}
    )