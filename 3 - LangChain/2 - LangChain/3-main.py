import os
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from langchain_core.globals import set_debug
    
set_debug(True)
    
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
sys.stdout.reconfigure(encoding="utf-8")

class Destino(BaseModel):
    cidade: str = Field(description="A cidade recomendada para visitar")
    motivacao: str = Field(description="O motivo pelo qual e interessante visitar essa cidade")


class Restaurante(BaseModel):
      cidade: str = Field(description="A cidade recomendada para visitar")
      restaurantes: str = Field(description="RestauranteS recomendado nada cidade")


parseador_destino = JsonOutputParser(pydantic_object=Destino)
parseador_restaurante = JsonOutputParser(pydantic_object=Restaurante)

prompt_cidade = PromptTemplate(
    template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    {formato_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formato_de_saida": parseador_destino.get_format_instructions()},
)

prompt_restaurantes = PromptTemplate(
    template="""
    Sugira restaurantes recomendados para visitar na cidade {cidade}.
    {formato_de_saida}
    """,
    partial_variables={"formato_de_saida": parseador_restaurante.get_format_instructions()},
)

promtp_cultural = PromptTemplate(
    template="""
    Sugira atividades culturais e locais culturais para visitar na cidade {cidade}.
    """,
)

modelo = ChatGroq(
    groq_api_key=api_key,
    model="openai/gpt-oss-120b",
    temperature=0.5,
)

cadeia_1 = prompt_cidade | modelo | prompt_cidade
cadeia_2 = prompt_restaurantes | modelo | prompt_restaurantes
cadeia_3 = promtp_cultural | modelo | StrOutputParser()

cadeia = (cadeia_1 | cadeia_2 | cadeia_3)

resposta = cadeia.invoke({"interesse": "praias"})
print(resposta)