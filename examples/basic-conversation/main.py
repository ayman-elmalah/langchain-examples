from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

messages = [
    SystemMessage(content="Solve the following problem"),
    HumanMessage(content="What is 100 divided by 20")
]

result = model.invoke(messages)

print(result.content)

