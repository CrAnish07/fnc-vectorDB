from config import settings
from db.add_documents import add_docs
from db.view_documents import view_docs
from db.search_documents import search_docs_with_score, search_with_filter
from db.update_documents import update_docs
from db.delete_documents import delete_docs

if __name__ == "__main__":
    add_docs()

    print(view_docs())

    print(search_docs_with_score("QUERY", k=2))
    print(search_with_filter())

    update_docs()
    print(view_docs())

    delete_docs()
    print(view_docs())