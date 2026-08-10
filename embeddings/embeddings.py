import openai

try:
    from openai import OpenAI
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
    )
except ImportError:
    client = None
    openai.api_key = "ollama"
    openai.api_base = "http://localhost:11434/v1"


def create_embeddings(text: str):
    if client is not None:
        embedding_response = client.embeddings.create(
            model="nomic-embed-text-v2-moe",
            input=text
        )
    else:
        embedding_response = openai.Embedding.create(
            model="nomic-embed-text-v2-moe",
            input=text
        )

    return embedding_response.data[0].embedding



