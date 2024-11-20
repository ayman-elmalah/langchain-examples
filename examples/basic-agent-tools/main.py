from dotenv import load_dotenv

from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain import hub
from langchain_openai import ChatOpenAI

load_dotenv()

def get_current_time(*args, **kwargs):
    """Returns the current time in H:MM AM/PM format."""
    import datetime  # Import datetime module to get current time

    now = datetime.datetime.now()  # Get current time
    return now.strftime("%I:%M %p")  # Format time in H:MM AM/PM format

def perform_calculation(query: str, *args, **kwargs):
    """Performs a basic calculation based on the query."""
    try:
        return str(eval(query))
    except Exception as e:
        return f"Error: {str(e)}"

tools = [
    Tool(
        name="Time",
        func=get_current_time,
        description="Useful for when you need to know the current time",
    ),
    Tool(
        name="Calculator",
        func=perform_calculation,
        description="Useful for performing basic calculations. Input should be a valid Python expression.",
    )
]

prompt = hub.pull("hwchase17/react")

llm = ChatOpenAI(model="gpt-3.5-turbo")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
    stop_sequence=True
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
)

response = agent_executor.invoke({"input": "What time is it?"})
print("Response to time query:", response)

# response= agent_executor.invoke({"input": "What is 5 + 7 * 2?"})
# print("Response to calculation query:", response)
