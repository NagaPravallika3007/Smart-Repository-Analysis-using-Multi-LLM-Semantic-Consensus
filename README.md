# Smart-Repository-Analysis-using-Multi-LLM-Semantic-Consensus
Smart Repository Analysis using Multi-LLM Semantic Consensus
📌 Overview

Smart Repository Analysis using Multi-LLM Semantic Consensus is an AI-powered GitHub repository understanding system that analyzes source code using multiple Large Language Models (LLMs) and generates high-quality answers through semantic consensus reasoning.

The system allows users to upload or provide a GitHub repository URL and ask natural language questions about the codebase. It combines Retrieval-Augmented Generation (RAG), semantic search, vector embeddings, and multi-model AI reasoning to improve response accuracy and reduce hallucinations.

This project helps developers, students, and teams quickly understand unfamiliar repositories without manually reading thousands of lines of code.

🚀 Features
🔍 GitHub Repository Analysis
🧠 Multi-LLM Semantic Consensus
📚 Retrieval-Augmented Generation (RAG)
🔎 Semantic Code Search
💬 Natural Language Repository Q&A
⚡ Streamlit Interactive UI
🗂️ Repository Caching System
📦 Vector Database Integration
🧩 Code Chunking & Embeddings
🤖 AI-Powered Code Understanding
🌐 GitHub URL Processing
📊 Intelligent Context Retrieval
🏗️ System Architecture
GitHub Repository
        ↓
Repository Cloning
        ↓
Code Extraction & Chunking
        ↓
Embedding Generation
        ↓
Vector Database Storage
        ↓
Semantic Retrieval
        ↓
Multiple LLM Processing
        ↓
Semantic Consensus Engine
        ↓
Final Intelligent Response
🛠️ Tech Stack
Frontend
Streamlit
Backend
Python
AI / ML
LangChain
OpenAI API
Gemini API
Ollama
Sentence Transformers
Vector Database
ChromaDB / FAISS
Other Tools
GitHub API
dotenv
GitPython

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/NagaPravallika3007/Smart-Repository-Analysis-using-Multi-LLM-Semantic-Consensus.git
2️⃣ Navigate to the Project Directory
cd Smart-Repository-Analysis-using-Multi-LLM-Semantic-Consensus
3️⃣ Create Virtual Environment
Windows
python -m venv .venv

Activate environment:

.venv\Scripts\activate
Linux / Mac
python3 -m venv .venv
source .venv/bin/activate
📦 Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the root directory.

OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
▶️ Run the Application
streamlit run app.py
💡 How It Works
User enters a GitHub repository URL.
Repository is cloned locally.
Source code files are extracted and chunked.
Embeddings are generated for code chunks.
Embeddings are stored in a vector database.
User asks questions about the repository.
Relevant context is retrieved using semantic search.
Multiple LLMs analyze the retrieved context.
Semantic consensus engine combines responses.
Final intelligent answer is displayed to the user.
🧠 Semantic Consensus Mechanism

The project uses multiple LLMs to generate different perspectives for the same query.

The semantic consensus engine:

compares responses,
evaluates semantic similarity,
identifies the most accurate insights,
and generates a final refined response.

This improves:

Answer reliability
Context understanding
Hallucination reduction
Response quality
📊 Example Use Cases
Understanding unfamiliar GitHub repositories
AI-powered codebase documentation
Developer onboarding assistance
Repository summarization
Bug investigation support
Architecture understanding
Code explanation and navigation
🎯 Future Enhancements
🔄 Real-time repository monitoring
👥 Multi-agent AI collaboration
📈 Repository analytics dashboard
🧾 Automatic documentation generation
🐳 Docker deployment
☁️ Cloud hosting support
🔐 Authentication system
🗣️ Voice-based repository interaction
📸 Screenshots

Add application screenshots here.

assets/screenshots/
👩‍💻 Author

U. Naga Pravallika
B.Tech – Artificial Intelligence & Machine Learning

📜 License

This project is developed for educational and research purposes.

⭐ Acknowledgements
OpenAI
Google Gemini
LangChain
Streamlit
ChromaDB
Hugging Face
GitHub API
📬 Contact

For suggestions or collaboration:

GitHub: https://github.com/NagaPravallika3007
