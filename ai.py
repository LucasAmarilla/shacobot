from langchain.prompts import ChatMessagePromptTemplate
from langchain_ollama import OllamaLLM

# Definindo o template do prompt
template = """
Responda a pergunta em português como se voce fosse o personagem {personagem} do League of Legends de forma curta, direta e sem descrição.

Aqui está o histórico da conversa:
{context}

Pergunta: {question}

Resposta:
"""

prompt = ChatMessagePromptTemplate.from_template(template, role="user")

# Configurando o modelo
model = OllamaLLM(model='llama3.2')

def chama_na_conversa(context: str, question: str, personagem: str):
    context = context
    inputs = {"context": context, "question": question, "personagem": personagem}
    formatted_prompt = prompt.format(**inputs).content  

    res = model.invoke(formatted_prompt)
    return res


#Script de loop padrão
# def conversinha():
#     context = ""
#     print("escreve palhaco para sair")
#     while True:
#         userInput = input("Você: ")
#         if userInput == "palhaco":
#             break
#         inputs = {"context": context, "question": userInput}
#         formatted_prompt = prompt.format(**inputs).content  # Extrai o conteúdo como string

#         res = model.invoke(formatted_prompt)

#         print("Shaco: ", res)
#         context += f"Você: {userInput}\nShaco: {res}\n"
    
