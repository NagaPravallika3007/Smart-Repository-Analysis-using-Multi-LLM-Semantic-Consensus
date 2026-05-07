# Smart Repository Analysis using Multi-LLM Semantic Consensus

## 📌 Overview

Smart Repository Analysis using Multi-LLM Semantic Consensus is an AI-powered GitHub repository understanding system that analyzes source code using multiple Large Language Models (LLMs) and generates intelligent responses using semantic consensus reasoning.

The system allows users to upload or provide a GitHub repository URL and ask natural language questions about the codebase.

---

## 🚀 Features

- GitHub Repository Analysis
- Multi-LLM Semantic Consensus
- Retrieval-Augmented Generation (RAG)
- Semantic Code Search
- Natural Language Repository Q&A
- Streamlit Interactive UI
- Repository Caching
- Vector Database Integration

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI/ML
- LangChain
- OpenAI
- Gemini
- Ollama
- Sentence Transformers

### Vector Database
- ChromaDB / FAISS

---

## 📂 Project Structure

```bash
Smart-Repository-Analysis/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── src/
├── data/
├── cache/
└── chroma_db/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/NagaPravallika3007/Smart-Repository-Analysis-using-Multi-LLM-Semantic-Consensus.git
```

### Navigate to Project

```bash
cd Smart-Repository-Analysis-using-Multi-LLM-Semantic-Consensus
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
GEMINI_API_KEY=your_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. User enters GitHub repository URL
2. Repository gets cloned
3. Source code is chunked
4. Embeddings are generated
5. Vector database stores embeddings
6. Semantic retrieval fetches relevant context
7. Multiple LLMs analyze context
8. Semantic consensus generates final response

---

## 🎯 Future Enhancements

- Multi-agent AI collaboration
- Automatic documentation generation
- Cloud deployment
- Docker support
- Repository analytics dashboard

---

## 👩‍💻 Author

U. Naga Pravallika  
B.Tech – AIML

---

## ⭐ Acknowledgements

- OpenAI
- LangChain
- Streamlit
- ChromaDB
- Hugging Face
