from flask import Flask, render_template, request
from google import genai
from langchain_community.vectorstores import FAISS
from store_index import embeddings
from store_index import client, embeddings, vectorstores 

app = Flask(__name__)

def generate_answer(question):
    context = vectorstores.similarity_search(question, k=3)
    context_general = "\n\n".join([doc.page_content for doc in context]) if context else ""

    prompt = f"""
    Your name is "MediGuide", an intelligent medical assistant.

    Use **only** the information provided below to accurately and concisely answer the user's question. 

    Question:
    {question}

    Available Information:
    {context_general}

    Answer:
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text.strip()

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    try:
        msg = request.form["msg"]
        print("User:", msg)
        answer = generate_answer(msg)
        return str(answer)

    except Exception as e:
        print("Error:", e)
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
