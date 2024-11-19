from dotenv import load_dotenv
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

template = "Give me top {count} players in {region}"
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI(model="gpt-3.5-turbo")

chain = prompt | model

result = chain.invoke({"count": 5, "region": "africa"})

print(result.content)
