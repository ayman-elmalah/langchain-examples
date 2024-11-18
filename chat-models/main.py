from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")
response = model.invoke("What is the capital of egypt?")

print(response.content)
