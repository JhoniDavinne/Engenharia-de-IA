import os
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from langchain_core.globals import set_debug
    
set_debug(True)
    
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
sys.stdout.reconfigure(encoding="utf-8")

class Destino(BaseModel):
    cidade: str = Field(description="A cidade recomendada para visitar")
    motivacao: str = Field(description="O motivo pelo qual e interessante visitar essa cidade")

parseador = JsonOutputParser(pydantic_object=Destino)

prompt_cidade = PromptTemplate(
    template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    {formato_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formato_de_saida": parseador.get_format_instructions()},
)

modelo = ChatGroq(
    groq_api_key=api_key,
    model="openai/gpt-oss-120b",
    temperature=0.5,
)

cadeia = prompt_cidade | modelo | parseador

resposta = cadeia.invoke({"interesse": "praias"})
print(resposta)