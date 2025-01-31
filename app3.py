from langchain.agents import initialize_agent, AgentType
from langchain.agents import Tool
from langchain.llms import HuggingFaceHub
from duckduckgo_search import ddg_search

# Define DuckDuckGo search tool using duckduckgo-search
def search_duckduckgo(query: str):
    search_results = ddg_search(query)
    if search_results:
        # Returning the first result's snippet as the answer
        return search_results[0]['body'] if search_results else "No answer found."
    return "No answer found."

duckduckgo_tool = Tool(
    name="DuckDuckGo Search",
    func=search_duckduckgo,
    description="Use DuckDuckGo to search the web."
)

# Initialize the Hugging Face model (Replace with the model you prefer from Hugging Face)
llm = HuggingFaceHub(
    repo_id="distilbert-base-uncased",  # Example: You can change this to another Hugging Face model
    model_kwargs={"temperature": 0.7}
)

# Initialize agent with tools
tools = [duckduckgo_tool]
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent with your query
query = "Who is the CEO of DeepSeek AI?"
response = agent.run(query)
print(response)
