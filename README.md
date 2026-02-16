AI Debugger Copilot — Multi-Agent RAG System for Java Errors

An intelligent debugging assistant that analyzes Java errors, retrieves relevant knowledge, generates fixes, validates solutions, and learns from past debugging sessions.

This project demonstrates a production-style multi-agent AI architecture combining Retrieval-Augmented Generation (RAG), reranking, planning agents, and memory-based learning.

🚀 What this project does

Given a Java error like:

ConcurrentModificationException in ArrayList loop


The system:

Understands the error using an AI analyst agent

Plans how to search using a retrieval strategist agent

Retrieves knowledge from vector database

Reranks results using a cross-encoder

Generates multiple fixes with explanation

Validates the solution using a reviewer agent

Learns from the debugging session using memory

🧠 System Architecture
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

🤖 Agents in the System
1️⃣ Error Analyst

Extracts exception type

Identifies domain

Predicts root cause signals

2️⃣ Retrieval Strategist

Plans search depth

Expands queries

Chooses retrieval strategy

3️⃣ Fix Generator

Produces multiple solution approaches

Recommends best fix

Provides step-by-step actions

4️⃣ Solution Validator

Reviews fix correctness

Checks logical consistency

Adds reviewer feedback

5️⃣ Memory Agent

Stores past debugging sessions

Retrieves similar past errors

Improves system performance over time

🔍 Tech Stack
AI / ML

Retrieval Augmented Generation (RAG)

Sentence Transformers

FAISS vector search

Cross-Encoder reranking

Multi-agent orchestration

Backend

Python

Groq / LLM APIs

Modular agent architecture

📊 Key Features

✔ Multi-agent reasoning pipeline
✔ Vector similarity search
✔ Cross-encoder reranking
✔ Solution validation layer
✔ Memory-based learning
✔ Structured debugging outputs

🧪 Example Output
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
Reviewer note: Recommended fix is safe and appropriate

🧠 Learning Capability

The system stores:

past errors

successful fixes

validation confidence

Future similar errors trigger:

MEMORY HIT FOUND


and reuse learned solutions instantly.

💼 Why this project matters

This is not a chatbot.

It demonstrates:

AI system architecture

retrieval planning

reasoning agents

ML feedback loops

production-style debugging assistant design

Suitable for roles in:

Generative AI Engineering

Machine Learning Engineering

Applied AI

AI Platform Engineering

🛠️ How to Run
1️⃣ Clone repo
git clone <repo-url>
cd ai-debugger

2️⃣ Create virtual environment
python -m venv .venv
source .venv/Scripts/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add API key

Create .env

GROQ_API_KEY=your_key_here

5️⃣ Run app
python app.py

📌 Future Improvements

Streamlit UI

Real-time IDE plugin

Codebase-level debugging

Performance benchmarking

Reinforcement learning for fix ranking

👩‍💻 Author

Built as part of AI engineering and ML portfolio.

Focus areas:

Multi-agent AI systems

Retrieval-based reasoning

Learning copilots

Developer productivity AI

⭐ If you found this useful

Star the repo — it helps visibility and supports the project.
