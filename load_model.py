# ----- LLM MODEL -----

from langchain_ollama import ChatOllama

# Initialize the LLM (choose one of these models)
llm = ChatOllama(
    model="llama3.2",
    num_gpu=1,
    temperature=0.2,   # Lower for factual responses
    top_p=0.9,  # Nucleus sampling parameter
    system="You are a helpful assistant specialized in City of Kitchener information.",  # System prompt
    timeout=120,  # Longer timeout for complex queries
    num_ctx=4096,  # Larger context window
    num_thread=8,  # Use more CPU threads
    format="json",  # Force structured output when needed
    keep_alive="5m",  # Keep model loaded for 5 minutes
)

# Test the model
# response = llm.invoke("What is 2+2?")
# print(response)