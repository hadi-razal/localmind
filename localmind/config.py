from pydantic import BaseModel


class Settings(BaseModel):
    llm_model:str = 'llama3.1:8b'
    system_prompt:str = (
        "You are a helpfull AI assistant that creates localmind for the user. and you name is localmind and you are create by Hadi Razal"
    )

settings = Settings()