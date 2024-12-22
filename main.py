from ai import chama_na_conversa
from fastapi import FastAPI
from pydantic import BaseModel

class Base(BaseModel):
    context: str
    question: str
    personagem: str

app = FastAPI()

@app.get("/")
def root(base: Base):
    return chama_na_conversa(base.context, base.question, base.personagem)