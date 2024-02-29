import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()


template = '''Given the {information} about person. 
              I want you to create: 
              1. A short summary; 
              2. Two interesting facts about given person'''

prompt = PromptTemplate(input_variables=["information132", 'ingi'], template=template)
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
chain = LLMChain(llm=llm, prompt=prompt)

information = 'Christiano Ronaldo'
result = chain.invoke(input={'information': information, '1': 'elon musk'})
print(result)
print(prompt)