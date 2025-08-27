from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI

agent = initialize_agent(
    tools=[my_tool], 
    llm=OpenAI(temperature=0), 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)
result = agent.run("What is 7 * 9?")
print(result)
