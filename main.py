import os

from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
# tavily import TavilyClient
from langchain_tavily import TavilySearch

# tavily = TavilyClient()


llm = ChatOpenAI(model="deepseek-chat", base_url=os.getenv("OPENAI_BASE_URL"))
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {"messages": HumanMessage(content="What is the weather in San Francisco?")}
    )
    print(result)


if __name__ == "__main__":
    main()
