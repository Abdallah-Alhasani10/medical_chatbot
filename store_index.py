from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader,DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List
from google import genai
from src.helper import load_pdf,text_splitter,download_hugging_face_embddings,filter_to_minimal_docs
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=os.environ.get('api_giminai')
client = genai.Client(api_key=API_KEY)

extracted_data = load_pdf(r"C:\Users\Lenovo\Desktop\Medical_chatbot\data")
minimal_docs=filter_to_minimal_docs(extracted_data)
text_chunks=text_splitter(minimal_docs)
embeddings=download_hugging_face_embddings()
vectorstores = FAISS.load_local(
    folder_path="faiss_index_loacl",
    embeddings=embeddings,
    allow_dangerous_deserialization=True
)