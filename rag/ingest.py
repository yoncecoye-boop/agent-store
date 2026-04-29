from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os
from config import CHROMA_PATH

def load_documents(data_path="./data/docs"):
    docs = []
    for file in os.listdir(data_path):
        path = os.path.join(data_path, file)
        if file.endswith(".pdf"):
            docs.extend(PyPDFLoader(path).load())
        elif file.endswith(".txt"):
            docs.extend(TextLoader(path).load())
    return docs

def ingest():
    docs = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=CHROMA_PATH
    )

    db.persist()
    print("✅ 文档入库完成")

if __name__ == "__main__":
    ingest()
