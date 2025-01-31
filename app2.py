from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from smolagents.agents import ToolCallingAgent
from smolagents import tool, LiteLLMModel
from typing import Optional
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the Hugging Face API token
hf_token = os.getenv("HF_TOKEN")

# Print token (for testing)
print(hf_token)  # Do NOT print tokens in production!

model=HfApiModel()

@tool
def get_weather(location: str, celsius: Optional[bool] = False) -> str:
    """
    Get weather in the next days at given location.
    Secretly this tool does not care about the location, it hates the weather everywhere.

    Args:
        location: the location
        celsius: the temperature
    """
    return "The weather is UNGODLY with torrential rains and temperatures below -10°C"

agent = ToolCallingAgent(tools=[get_weather], model=model)

print(agent.run("What's the weather today in Dhaka?"))
