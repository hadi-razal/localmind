from pathlib import Path
import chromadb

from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama


class RagQuery:
    def __init__(
        self,
        persist_dir: str = "storage/chroma",
        collection_name: str = "rag_collection",
        embed_model_name: str = "all-MiniLM-L6-v2",
        llm_model: str = "llama3:8b-instruct-q4_0"
    ):
        
        self.persist_dir = Path(persist_dir)
        self.collection_name = collection_name
        self.embed_model = HuggingFaceEmbedding(model_name=embed_model_name)
        self.llm = Ollama(model=llm_model, request_timeout=120.0)

    def ask(self, question: str, top_k: int = 5):
        
        client = chromadb.PersistentClient(path=str(self.persist_dir))
        collection = client.get_or_create_collection(name=self.collection_name)
        
        # Check if collection is empty
        if collection.count() == 0:
            raise ValueError(
                f"Collection '{self.collection_name}' is empty. "
                "Please build the index first using RagIndexer.build()"
            )
        
        vector_store = ChromaVectorStore(chroma_collection=collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        
        index = VectorStoreIndex.from_vector_store(
            vector_store=vector_store,
            storage_context=storage_context,
            embed_model=self.embed_model,
        )
        
       
        query_engine = index.as_query_engine(
            llm=self.llm,
            similarity_top_k=top_k,
        )

        response = query_engine.query(question)

        return response