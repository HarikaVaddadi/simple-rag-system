# Simple RAG System

A beginner-friendly Retrieval Augmented Generation (RAG) application that allows users to ask questions about documents.

The system retrieves relevant information from documents and provides grounded answers using an LLM.

---

## What is RAG?

RAG (Retrieval Augmented Generation) combines:

1. Retrieval from a knowledge base
2. Generation using a Large Language Model (LLM)

Instead of relying only on the model's training data, the model receives relevant document context before generating an answer.

---

## Architecture

```text
Documents
    |
    v
Chunking
    |
    v
Embeddings
    |
    v
Vector Database (FAISS)
    |
    v
Retriever
    |
    v
LLM
    |
    v
Answer
```

---

## Example

### Document

```text
Policy Number: ABC123

Date of Loss: 12 January 2025

Response Deadline: 30 days

Claim Amount: $5000
```

### User Question

```text
What is the response deadline?
```

### Retrieved Context

```text
Response Deadline: 30 days
```

### Answer

```text
The response deadline is 30 days.
```

---

## Project Structure

```text
simple-rag/
│
├── data/
│   └── insurance_policy.txt
│
├── src/
│   ├── ingest.py
│   ├── retrieve.py
│   └── rag.py
│
├── requirements.txt
├── README.md
```

---

## Components

### 1. Document Loader

Loads text or PDF documents.

Example:

```text
insurance_policy.txt
```

---

### 2. Chunking

Splits large documents into smaller chunks.

Benefits:

* Better retrieval
* Faster search
* Improved accuracy

---

### 3. Embeddings

Converts text into vectors.

Example:

```text
"Response Deadline"
       ↓
[0.12, 0.45, 0.88, ...]
```

These vectors help identify semantically similar content.

---

### 4. Vector Database

Stores document embeddings.

In this project:

```text
FAISS
```

Responsibilities:

* Store vectors
* Similarity search
* Fast retrieval

---

### 5. Retriever

Finds the most relevant chunks for a user query.

Example:

```text
Question:
What is the response deadline?

Retrieved Chunk:
Response Deadline: 30 days
```

---

### 6. LLM

Uses retrieved context to generate the final answer.

Prompt:

```text
Context:
Response Deadline: 30 days

Question:
What is the response deadline?
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd simple-rag
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 1: Create Embeddings

```bash
python src/ingest.py
```

Creates:

```text
faiss_index/
```

---

### Step 2: Test Retrieval

```bash
python src/retrieve.py
```

Retrieves relevant document chunks.

---

### Step 3: Run RAG Pipeline

```bash
python src/rag.py
```

Example:

```text
Question:
What is the response deadline?

Answer:
The response deadline is 30 days.
```

---

## Key Concepts Demonstrated

* Retrieval Augmented Generation (RAG)
* Document Chunking
* Embeddings
* Vector Databases
* Similarity Search
* Prompt Engineering
* Grounded Generation

---

## Interview Discussion Points

This project can be used to explain:

* What is RAG?
* Why RAG instead of fine-tuning?
* What are embeddings?
* What is FAISS?
* What is chunking?
* How does retrieval work?
* How does RAG reduce hallucinations?

---

## Future Enhancements

### Version 2

* PDF Support
* Multiple Documents
* Metadata Filtering

### Version 3

* Hybrid Search
* Reranking
* Query Expansion

### Version 4

* Streamlit UI
* Chat Interface
* Document Upload

---

## Key Takeaway

RAG improves answer quality by retrieving relevant information from documents and providing that context to the LLM before generating a response.
