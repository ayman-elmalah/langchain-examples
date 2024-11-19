from dotenv import load_dotenv
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a comedian who tells jokes about {topic}"),
    ("human", "Tell me {jokes_count} jokes")
])

model = ChatOpenAI(model="gpt-3.5-turbo")

chain = prompt | model | StrOutputParser()

result = chain.invoke({"topic": "Programmers", "jokes_count": "2"})

print(result)
