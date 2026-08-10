import os
import sys
from openai import OpenAI

sys.path.append(os.path.abspath(os.path.join('..')))

from embeddings.embeddings import create_embeddings
import chromadb

INTENT_PROMPT = '''Classify the following user input as 'CHAT' or 'RAG'. Respond only as 'CHAT' or 'RAG'.

- Use 'CHAT' if the input is a greeting, small talk, pleasantry, or goodbye.
- Use 'RAG' if the input is asking for specific facts, documents, data, or technical information.

Hi! How are you? > 'CHAT'
What is the result of match number 1? > 'RAG'
Hi! > 
'''

client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
)

def create_context(query_: str):

    intent_prompt =  INTENT_PROMPT

    response = client.chat.completions.create(
        model='llama3.2:1b',
        messages=[{'role':'system', 'content':intent_prompt},
                  {'role':'user', 'content':query_}],
        temperature=0.0
    )

    message = getattr(response.choices[0], 'message', None)

    if 'CHAT' in message.content:
        return "Hi! I am your assistant. I am your cricketing assistant. Here, to answer your questions"   

    result_query = create_embeddings(query_)

    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    collection = chroma_client.get_or_create_collection(name="rag_collection")

    results = collection.query(
        query_embeddings=[result_query],
        n_results=5,
        include=["documents","metadatas"]
    )

    context_chunks = results['documents'][0]
    return " ".join(context_chunks)
