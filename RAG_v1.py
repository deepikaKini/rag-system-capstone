import sqlite3
import os
import torch
import faiss
from transformers import AutoTokenizer, AutoModel
import google.generativeai as genai

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Configure Gemini API key
# genai.configure(api_key="AIzaSyDBZYnMzqNnkka9eaOtp5T41NMRpoOGYHI")

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")
genai.configure(api_key=api_key)
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

# Function to fetch documents from the SQLite database based on a specific topic
def fetch_data():
    conn = sqlite3.connect('CapstoneV1.db')
    cursor = conn.cursor()

    # Fetch all student documents
    cursor.execute("SELECT topic, content, studentid FROM student_documents")
    student_documents = [{"topic": row[0], "content": row[1], "student_id": row[2]} for row in cursor.fetchall()]

    # Fetch all reference documents
    cursor.execute("SELECT topic, content FROM reference_documents")
    reference_documents = [{"topic": row[0], "content": row[1]} for row in cursor.fetchall()]

    conn.close()
    return student_documents, reference_documents



# Load pre-trained sentence transformer model
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

# Function to embed documents
def embed_documents(documents):
    inputs = tokenizer([doc['content'] for doc in documents], padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].numpy()  # Use the [CLS] token embedding

# Retrieval function for top_k similar documents
def retrieve(query, index, documents, top_k=3):
    query_embedding = embed_documents([{"content": query}])
    distances, indices = index.search(query_embedding, top_k)
    print(distances, indices)

    return [documents[i] for i in indices[0]]

# Function to generate an answer using Gemini
def generate_answer(context, query):
    prompt = f"Answer briefly based on the context:\n\nContext: {context}\n\nQuestion: {query}"
    response = gemini_model.generate_content(prompt)
    return response.text

# Compare student and reference documents and find missing content
# def compare_notes(student_docs, ref_docs):
#     missing_content = []
#     for ref_doc in ref_docs:
#         if not any(ref_doc['content'] in student_doc['content'] for student_doc in student_docs):
#             missing_content.append(ref_doc['content'])
#     return missing_content

# RAG Pipeline: Retrieve documents and generate answers for the query
def rag_pipeline(query, student_docs, ref_docs, index):
    retrieved_docs = retrieve(query, index, student_docs + ref_docs)
    context = " ".join([doc['content'] for doc in retrieved_docs])

    # missing_notes = compare_notes(student_docs, ref_docs)
    # missing_context = " ".join(missing_notes)

    # Debugging: Print the retrieved documents to verify correctness
    print("\n--- Retrieved Documents ---")
    for doc in retrieved_docs:
        print(doc['content'])

    answer = generate_answer(context, query)
    # missing_info = generate_answer(missing_context, query)

    return answer

# Main execution
if __name__ == "__main__":
    while True:

        # Fetch only documents related to the specified topic
        student_documents, reference_documents = fetch_data()

        student_notes = "\n".join([f"Student notes: {doc['topic'],doc['content'], doc['student_id']}" for doc in student_documents])
        reference_notes = "\n".join([f"Reference notes: {doc['topic'],doc['content']}" for doc in reference_documents])

        documents = student_notes + "\n" + reference_notes
        print(documents)

        documents = student_documents + reference_documents

        document_embeddings = embed_documents(documents)

        # Build the FAISS index for document retrieval
        index = faiss.IndexFlatL2(document_embeddings.shape[1])
        index.add(document_embeddings)

        topic = input("Enter the topic you want to query: ")

        if not student_documents:
            print(f"No documents found for topic: {topic} in students notes")
            continue
        if not reference_documents:
            print(f"No documents found for topic: {topic} in reference notes")
            continue
        print(f"\nWelcome to the RAG System for {topic}!")
        print("You can now ask questions. Type 'exit' to end.")

        while True:
            query = input("\nEnter your query for the topic (or type 'exit' to end): ")

            if query.lower() == 'exit':
                print("Exiting the RAG system. Goodbye!")
                break
            query += f" for topic: {topic}"
            # Run the RAG pipeline
            answer = rag_pipeline(query, student_documents, reference_documents, index)

            # Print the RAG output and missing content details
            print("\nRAG Answer:")
            print(answer)
            # print("\nMissing Content in Student Notes:")
            # print(missing_info)
