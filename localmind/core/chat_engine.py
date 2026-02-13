from typing import List,Dict
from localmind.llm.client import LLMClient,Message
from localmind.config import settings

class ChatEngine: 
    
    def __init__(self):
        self.client = LLMClient(settings.llm_model)
        
        self.history: List[Message] = [
            {"role": "system", "content": settings.system_prompt}
        ]
        
    def ask(self, user_text: str) -> str:

        # 1. Add user message to history
        self.history.append({
            "role": "user",
            "content": user_text
        })

        # 2. Send entire history to model
        answer = self.client.chat(self.history)

        # 3. Add assistant reply to history
        self.history.append({
            "role": "assistant",
            "content": answer
        })

        return answer