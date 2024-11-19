from dotenv import load_dotenv
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

template = "Give me top {count} players in {region}"
prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({"count": 5, "region": "world"})

model = ChatOpenAI(model="gpt-3.5-turbo")
result = model.invoke(prompt)

print(result.content)