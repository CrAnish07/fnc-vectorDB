from langchain.schema import Document
from db.initialize_store import get_vector_store

def update_docs():
    store = get_vector_store()
    updated_doc = Document(
        page_content="Player INFO",
        metadata={"team":"TEAM"}
    )
    store.update_document(document_id='ID', document=updated_doc)