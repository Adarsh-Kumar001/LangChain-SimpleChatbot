import streamlit as st                       # streamlit used to create websites in python with minimal code and no frontend knowledge
from dotenv import load_dotenv               # reads the .env file, like ChatGoogleGenerativeAI reads GOOGLE_API_KEY,which is name of gemini api key fixed
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# instantiate our model object and generate chat completions:
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt=ChatPromptTemplate.from_messages(   
    [
        ("system","You are a language translator bot which converts {input_language} to {output_language}"),
        ("human","{input}")
    ]
)



st.title('Langchain Language Translator - English to French')                       # heading of the website
input_text=st.text_input("Enter your sentense in English to translate here")        # takes input from user


output_parser=StrOutputParser()           # parse output in more readable format

chain=prompt|llm|output_parser            # create a chain, i.e. the order of process flow
  
if input_text:                            # if input text is provided, pass it to chain so that it goes to prompt first, then to llm then llm gives output_parser
    st.write(chain.invoke({
        'input_language':'English',        # all 3 fields required by the prompt
        'output_language':'French',
        'input':input_text}))


    
