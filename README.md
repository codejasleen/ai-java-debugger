# 🧠 AI Java Debugger Copilot

A multi-agent AI system that helps developers debug Java errors using Retrieval-Augmented Generation (RAG), reranking, validation, and memory-based learning.

This project simulates how real AI copilots reason, retrieve knowledge, generate fixes, verify them, and improve over time.

---

## 🚀 What it does

Given a Java error like:

ConcurrentModificationException in ArrayList loop

The system:

1. Understands the error using an AI analyst agent  
2. Plans retrieval strategy using a strategist agent  
3. Searches a vector database for relevant knowledge  
4. Reranks results using a cross-encoder  
5. Generates multiple fixes with explanation  
6. Validates the solution using a reviewer agent  
7. Learns from the debugging session using memory  

---

## 🧠 System Architecture

User Error  
↓  
Memory Lookup (past debugging cases)  
↓  
Error Analyst Agent  
↓  
Retrieval Strategist Agent  
↓  
Vector Search (FAISS)  
↓  
Cross-Encoder Reranker  
↓  
Fix Generator Agent  
↓  
Solution Validator Agent  
↓  
Memory Learning  
↓  
Final Debug Output  

---

## 🤖 Agents in the System

### Error Analyst
- Extracts exception type  
- Identifies domain  
- Predicts root cause  

### Retrieval Strategist
- Plans search depth  
- Expands search queries  
- Controls retrieval behaviour  

### Fix Generator
- Suggests multiple fixes  
- Recommends best approach  
- Provides step-by-step solution  

### Solution Validator
- Reviews correctness of fix  
- Ensures logical consistency  
- Adds reviewer feedback  

### Memory Agent
- Stores past debugging sessions  
- Retrieves similar past errors  
- Improves system performance over time  

---

## 🔍 Tech Stack

### AI / ML
- Retrieval Augmented Generation (RAG)  
- Sentence Transformers  
- FAISS vector database  
- Cross-encoder reranking  
- Multi-agent orchestration  

### Backend
- Python  
- Groq / LLM APIs  
- Modular service architecture  

---

## 📊 Key Features

- Multi-agent reasoning pipeline  
- Vector similarity search  
- Cross-encoder reranking  
- Solution validation  
- Memory-based learning  
- Structured debugging output  

---

## 🧪 Example Output

ROOT CAUSE:  
Modifying collection while iterating over it  

RECOMMENDED FIX:  
Use Iterator  

QUICK STEPS:  
- Create iterator  
- Replace loop  
- Use iterator.remove()  

VALIDATION:  
Root cause valid: True  
Fix correct: True  

---

## 🧠 Learning Capability

The system stores:

- past errors  
- successful fixes  
- validation confidence  

Future similar errors trigger:

MEMORY HIT FOUND  

and reuse learned solutions instantly.

---

## 💼 Why this project matters

This is not a simple chatbot.

It demonstrates:

- multi-agent AI architecture  
- retrieval planning  
- ML feedback loop  
- system design thinking  
- developer productivity AI  

Relevant for roles in:

- Generative AI Engineering  
- Machine Learning Engineering  
- Applied AI  
- AI Platform Engineering  

---

## 🛠️ How to Run

### 1. Clone repository

git clone https://github.com/codejasleen/ai-java-debugger.git  
cd ai-java-debugger  

### 2. Create virtual environment

python -m venv .venv  
source .venv/Scripts/activate  

### 3. Install dependencies

pip install -r requirements.txt  

### 4. Add API key

Create `.env` file

GROQ_API_KEY=your_key_here  

### 5. Run app

python app.py  

---
## 🚀 Deployment

This project is deployed on AWS EC2 and runs as a background service using **systemd**, making the API publicly accessible and always available.

---

### 🌐 Live API

Access the running backend:
http://EC2-PUBLIC-IP:8000/docs

---

### ⚙️ Deployment Architecture

- **Cloud:** AWS EC2 (Ubuntu)
- **API Framework:** FastAPI
- **Server:** Uvicorn
- **Process Manager:** systemd
- **Vector DB:** FAISS
- **Embeddings:** sentence-transformers
- **Reranker:** cross-encoder
- **LLM:** Groq / OpenAI API

---
## 📌 Future Improvements

- Streamlit UI  
- IDE plugin integration  
- Codebase-level debugging  
- Evaluation metrics  
- Reinforcement learning for fix ranking  

---

## 👩‍💻 Author

Built as part of AI engineering and machine learning portfolio work.

Focus areas:

- Multi-agent AI systems  
- Retrieval-based reasoning  
- Learning copilots  
- Developer productivity tools  

---

⭐ If you found this useful, consider starring the repo.
