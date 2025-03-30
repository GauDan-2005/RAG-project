# -----EMBED TEXT-----
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="llama3.2")

def get_embedding(text):
    return embeddings.embed_query(text).tolist()


# ----- VECTORE STORE -----

from langchain_milvus import Milvus

MILVUS_URI = "http://localhost:19530"
db_name = "rag_application"

vectorstore = Milvus(
    embedding_function=embeddings,
    connection_args={"uri": MILVUS_URI, "token": "root:Milvus", "db_name": db_name},
    index_params={"index_type": "FLAT", "metric_type": "L2"},
    consistency_level="Strong",
    drop_old=False,  # set to True if seeking to drop the collection with that name if it exists
)


# ----- INSERT DOCUMENTS -----

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from uuid import uuid4

from ingest import website_data

# 1. Configure Text Splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,          # Target chunk size in characters
    chunk_overlap=200,        # Overlap between chunks for context
    length_function=len,      # How to measure chunk size
    add_start_index=True      # Track original positions
)

# 2. Process and Chunk Documents
all_chunks = []
for url, content in website_data.items():
    if content:
        # Create initial document
        doc = Document(
            page_content=content,
            metadata={
                "url": url,
                "source": "kitchener.ca",
                "doc_id": str(uuid4())  # Unique ID for the original document
            }
        )
        
        # Split into chunks
        chunks = text_splitter.split_documents([doc])
        
        # Add chunk-specific metadata
        for i, chunk in enumerate(chunks):
            chunk.metadata.update({
                "chunk_id": str(uuid4()),
                "chunk_num": i+1,
                "total_chunks": len(chunks)
            })
        
        all_chunks.extend(chunks)

# 3. Insert into Milvus
if all_chunks:
    inserted_ids = vectorstore.add_documents(
        documents=all_chunks,
        ids=[chunk.metadata["chunk_id"] for chunk in all_chunks]  # Explicit chunk IDs
    )
    print(f"Inserted {len(inserted_ids)} chunks from {len(website_data)} URLs")
else:
    print("No valid chunks to insert")
