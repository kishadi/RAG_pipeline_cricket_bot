# RAG Pipeline Cricket Assistant

A retrieval-augmented generation (RAG) pipeline for cricket match information.

## Overview

This project ingests cricket match JSON data, stores embeddings in a Chroma vector database, and answers user questions by combining document retrieval with a chat model.

## Data Source

Link for the dataset https://cricsheet.org/ and store it as raw_data/ in the project directory.

## Key components

- `app.py` - Main interactive chatbot entrypoint.
- `context_builder/context_builder.py` - Builds context by classifying queries and fetching relevant documents from Chroma.
- `prompt_assistant/assistant.py` - Sends a chat completion request to the OpenAI-compatible client.
- `embeddings/embeddings.py` - Creates embeddings using the OpenAI-compatible Python library.
- `data_prep/data_prep.py` - Generates match and over summaries from raw JSON.
- `vector_storage/vector.py` - Adds embeddings and documents to a Chroma collection.
- `wrapper.py` - Batch ingestion script for raw JSON files in `raw_data/all_json`. This is run to create vector database.

## Requirements

- Python 3.9+ (recommended 3.12+)
- `requirements.txt`
- Local OpenAI-compatible API endpoint at `http://localhost:11434/v1`
- `chromadb` vector database

## Setup

1. Create and activate a Python virtual environment:

```bash
python -m venv venv
.\venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure your OpenAI-compatible service is running and reachable at:

- `http://localhost:11434/v1`
- API key: `ollama`

## Usage

### Run the chatbot

```bash
python app.py
```

Enter questions at the prompt. Type `N` or `n` to exit.

### Ingest raw match data

Run `wrapper.py` after placing JSON files in `raw_data/all_json`:

```bash
python wrapper.py
```

This will process each file, create embeddings for match and over summaries, and store them in the Chroma collection under `./chroma_db`.

## Notes

- `context_builder` classifies queries as `CHAT` or `RAG` and only performs retrieval for factual questions.
- `app.py` maintains an ongoing conversation context so follow-up questions can use prior responses.
- The code currently uses a hardcoded local API key and endpoint for an OpenAI-compatible service.

## Project structure

```
app.py
requirements.txt
wrapper.py
context_builder/
  context_builder.py
embeddings/
  embeddings.py
data_prep/
  data_prep.py
prompt_assistant/
  assistant.py
vector_storage/
  vector.py
raw_data/
  all_json/
```
