from os import path
from pathlib import Path

import chromadb

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

class RagIndexer:
    def __init__(
        self,
        data_dir: str = "data/inbox",
        persist_dir:str  = "storage/chroma",
        collection_name:str = "rag_collection",
        embedding_model_name:str = "all-MiniLM-L6-v2"
    ):
    
      self.data_dir = Path(data_dir)
      self.persist_dir = Path(persist_dir)
      self.collection_name = collection_name
      self.embedding_model_name = embedding_model_name
    
    def build(self)-> int:
        docs = SimpleDirectoryReader(self.data_dir).load_data()
        if not docs:
            raise ValueError("No documents found in the data directory")
        
        embedded_model = HuggingFaceEmbedding(model_name=self.embedding_model_name)
        client = chromadb.PersistentClient(path=str(self.persist_dir))
        
        collection = client.get_or_create_collection(name=self.collection_name)
        
        vector_store = ChromaVectorStore(chroma_collection=collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        
        VectorStoreIndex.from_documents(
            docs,
            storage_context=storage_context,
            embed_model=embedded_model,
        )
        
        return len(docs)
    
        
            
    
    
    
    