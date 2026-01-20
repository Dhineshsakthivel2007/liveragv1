import os
from langchain_groq import ChatGroq
from langchain.messages import HumanMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
llm=ChatGroq(api_key=api_key,model="moonshotai/kimi-k2-instruct-0905",temperature=0.0)
def generate_answer(prompt:str)->str:
    messages=[
        SystemMessage(content="you are a helpfull news assistant"),
        HumanMessage(content=prompt)
    ]
    response=llm.invoke(messages)
    return response.content