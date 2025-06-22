from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
import os

def build_vectorstore():
    file_path = os.path.join("data", "telecom_faq.txt")
    with open(file_path, "r") as f:
        data = f.read()

    docs = [Document(page_content=line) for line in data.split("\n") if line.strip()]
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("vectorstore")
