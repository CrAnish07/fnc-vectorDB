fnc-vectorDB is a LangChain-based vector database that leverages ChromaDB and OpenAI embeddings to store, search, update, and manage document collections.

```
langchain_chroma_project/
├── config/
│ └── settings.py # Environment variables (API key)
├── data/
│ └── documents.py # IPL player documents
├── db/
│ ├── initialize_store.py
│ ├── add_documents.py 
│ ├── view_documents.py 
│ ├── search_documents.py
│ ├── update_documents.py 
│ └── delete_documents.py 
└── main.py # Run all operations
```
