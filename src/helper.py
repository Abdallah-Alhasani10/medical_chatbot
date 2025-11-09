from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader,DirectoryLoader
from langchain_core.documents import Document
from typing import List
from google import genai
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS




def load_pdf(data_path):
    loader = DirectoryLoader(
        data_path,
        glob="*.pdf",
        loader_cls=PyMuPDFLoader
    )
    documents = loader.load()
    return documents



def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get('source')
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={'source': src}
            )
        )
    return minimal_docs

def text_splitter(chunks):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    text_chunks=text_splitter.split_documents(chunks)
    return text_chunks

def download_hugging_face_embddings():
    embeddings=HuggingFaceEmbeddings(model_name=r'C:\Users\Lenovo\Desktop\Medical_chatbot\all-MiniLM-L6-v2')
    return embeddings




