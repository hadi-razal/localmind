from typing import List,Dict
import ollama

Message = Dict[str,str] 

class LLMClient:

    def __init__(self, model: str):
        self.model = model
        
    def chat(self, messages: List[Message]) -> str:
        resp = ollama.chat(
            model=self.model,
            messages=messages
        )
        
        return resp["message"]["content"]