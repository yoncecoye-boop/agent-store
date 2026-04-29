from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from config import CHROMA_PATH

def get_retriever():
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=OpenAIEmbeddings()
    )
    return db.as_retriever(search_kwargs={"k": 3})
