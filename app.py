#  ----- EMBEDDED VECTOR STORE -----

from embed import vectorstore


# ----- LLM MODEL -----

from load_model import llm


# ----- RAG PIPELINE -----

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 1. Retriever from Milvus vectorstore
retriever = vectorstore.as_retriever(
    search_type="mmr",  # Max marginal relevance for balanced results
    search_kwargs={
        "k": 5,  # Number of chunks to retrieve
        "score_threshold": 0.7,  # Minimum relevance score
        "expr": 'source == "kitchener.ca"'  # Filter by your metadata
    }
)

# 2. RAG prompt template
source_template = """Answer using ONLY these facts:
{context}

Question: {question}

Format your answer as:
Answer: [your response]
Sources: [comma-separated URLs]"""

prompt = ChatPromptTemplate.from_template(source_template)

# Custom output parser to extract sources
def extract_sources(output):
    if "Sources:" in output:
        answer, sources = output.split("Sources:")
        return {"answer": answer.strip(), "sources": [s.strip() for s in sources.split(",")]}
    return {"answer": output, "sources": []}


# 3. Assemble the RAG chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | extract_sources
)

# 4. Test the full pipeline
# query = "What are the requirements for getting a building permit in Kitchener?"
# result = rag_chain.invoke(query)
# print(result)