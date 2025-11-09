# MediGuide — Medical Chatbot

**MediGuide** is a lightweight local medical Q&A web app that uses a **prebuilt FAISS vector index** and **Google Gemini AI** to answer user questions from a collection of medical PDFs.  

The UI is a small Flask app that sends user questions to a server, which retrieves related document chunks and asks the configured generative model to produce an answer using only the retrieved context.

---

## Key Features

- Flask-based chat UI (`templates/chat.html`, `static/style.css`).  
- Retrieval from a **FAISS vector index** stored in `faiss_medical_index/`.  
- Local **HuggingFace embeddings** (`src/helper.py`).  
- Uses **Google Generative AI SDK** via `from google import genai` for response generation.  

---

## Repository Structure

- app.py # Flask app and main entrypoint
- store_index.py # Helper script referencing utilities and showing index usage
- src/helper.py # PDF loading, text splitting, and embedding creation
- src/prompt.py # Default system prompt template
- faiss_medical_index/ # Prebuilt FAISS index directory (contains index.faiss)
- data/ # PDF source documents used to create/rebuild the index
- templates/ # Chat frontend templates
- static/ # CSS and JS for frontend
---

## Prerequisites

- Windows machine (project prepared on Windows).  
- Python 3.10+ recommended.  
- A Google Generative AI API key (`.env`).  
- If rebuilding the FAISS index locally, you need an embeddings backend (currently `src/helper.py` uses a local HuggingFace model).  

### Notes on FAISS and Windows

- Installing FAISS on Windows via pip can be tricky. Using **conda** is recommended:
```powershell
conda install -c conda-forge faiss-cpu

    ---

### Recommended Python Packages

It is recommended to create a virtual environment and install the necessary dependencies. The exact package names and versions may vary depending on your environment. The recommended packages include:

- `flask`
- `python-dotenv`
- `langchain`
- `langchain-community`
- `google-generative-ai`
- `sentence-transformers`
- `transformers`
- `faiss-cpu` (or use `conda` to install FAISS)

#### Example Setup (Windows PowerShell)

```powershell

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install flask python-dotenv langchain la

## Project Summary

**MediGuide** is a personal project developed by me to create a lightweight, local medical chatbot.  
The app allows users to ask questions about medical topics and receive accurate answers using a combination of **preprocessed PDFs**, a **FAISS vector index**, and **Google Generative AI**.  

All components, including PDF loading, text splitting, embeddings, vector search, and the Flask-based chat interface, were designed and implemented by me.  
This project serves as both a practical tool for exploring medical Q&A automation and a demonstration of integrating local document retrieval with modern AI models.
