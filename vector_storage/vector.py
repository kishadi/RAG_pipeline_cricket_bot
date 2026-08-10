import os
import chromadb
import uuid

def vector_db_storage(embeddings,json_data):

    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    collection = chroma_client.get_or_create_collection(name="rag_collection")


    unique_id = uuid.uuid4()

    doc_id = f"line_{unique_id}" 

    collection.add(
                ids=[doc_id],
                embeddings=[embeddings],
                documents=[json_data],
                # metadatas=[{"source": file_path, "line_number": index + 1}]
            )




