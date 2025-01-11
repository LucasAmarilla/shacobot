from ai import chama_na_conversa
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.getenv('AUTH_TOKEN')

class Base(BaseModel):
    token: str
    context: str
    question: str
    personagem: str

app = FastAPI()

@app.get("/chat")
def root(base: Base):
    if base.token != AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")
        
    return chama_na_conversa(base.context, base.question, base.personagem)