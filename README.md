# RAG Chatbot

This project implements a chatbot using **Chainlit, Langchain, Milvus, and OpenAI/LLaMA 3.3 (or another model)** to answer questions based on website content.

## Features
- **Retrieval-Augmented Generation (RAG)** for improved chatbot responses.
- **Milvus vector database** for efficient storage and retrieval of embeddings.
- **Langchain** for managing prompt engineering and model interactions.
- **Chainlit** for building an interactive chatbot UI.
- **Web Scraping** to extract content from websites for knowledge enrichment.

## Tech Stack
- **Frontend:** Chainlit
- **Backend:** Python (FastAPI/Flask)
- **Database:** Milvus
- **Embedding Model:** OpenAI/LLaMA 3.3
- **Orchestration:** Langchain

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

### 2. Create a Virtual Environment
```sh
python3 -m venv rag_env
source rag_env/bin/activate  # On Windows: rag_env\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file in the root directory and add:
```sh
OPENAI_API_KEY=your_openai_api_key
MILVUS_HOST=localhost
MILVUS_PORT=19530
```

### 5. Run Milvus (Vector Database)
If using Docker, start Milvus:
```sh
docker-compose up -d
```

### 6. Start the Application
```sh
python app.py
```

## Usage
1. Open the chatbot UI using Chainlit:
   ```sh
   chainlit run chainlit_app.py
   ```
2. Start chatting with the AI!

## Project Structure
```
📂 rag-chatbot
├── 📂 rag_env/               # Virtual environment (ignored in git)
├── 📂 milvus_data/           # Milvus database storage
├── 📂 volumes/               # Docker volumes
├── 📜 app.py                 # Main application file
├── 📜 chainlit_app.py        # Chainlit chatbot UI
├── 📜 embed.py               # Embedding generator
├── 📜 extract_content.py     # Web scraper for content extraction
├── 📜 extract_url.py         # URL extraction utility
├── 📜 ingest.py              # Data ingestion script
├── 📜 load_model.py          # Model loader
├── 📜 milv.py                # Milvus vector search implementation
├── 📜 delete_db.py           # Cleanup script
├── 📜 requirements.txt       # Project dependencies
├── 📜 docker-compose.yml     # Docker configuration
├── 📜 .env                   # Environment variables (ignored in git)
└── 📜 README.md              # Project documentation
```

## Contributing
Feel free to submit issues or pull requests to enhance the chatbot!

## License
This project is licensed under the MIT License.

