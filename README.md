# Imagination Engine
Imagination Engine is an agentic orchestration framework for rapidly building agentic architectures in Python. It accelerates agentic development, empowering developers to craft architectures that enable LLMs to excel in higher-order tasks like idea generation and critical thinking.

This library is designed to be used as a backend for AI apps and automations, providing support for all major LLM providers and locally-hosted model endpoints.

**This project is currently in development. More features and support coming very soon.**

# Getting Started
## Imports
Import the components you need:
```python
from imengine import Agent, Graph, START, END
```

## Setting Up Environment Variables
1. Copy the `.env.template` file to a new file named `.env`:
   ```bash
   cp .env.template .env
   ```

2. Fill in your API keys and configurations in the `.env` file:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

3. The library will automatically load these variables when needed. At minimum, you'll need the API key for your preferred LLM provider.

## Initalize Clients for LLM APIs
Done in the format standard to your API.

## Create Agents
Initalize the agents you'd like to call with a simple schema:
```
agent = Agent(
          client=client, 
          model="gpt-4o", 
          name="Agent", 
          system_prompt="You are a friendly assistant.",
          description="This agent is an example agent."
    )
```

## Define how agents are executed with a Graph
Graphs connect agents together using nodes and edges, routing the execution flow and all needed information through the graph. Each node represents an agent and each edge represents a conditional under which that agent is called. This conditional can be defined in natural language for each agent, within its `system_prompt`. 

In the case of multiple edges branching from one node, agents can understand their routing options using the `description` field of connecting nodes.

Every graph accepts user input at the `START` and returns a response to the user at the `END`.

With this basic understanding, a graph can be created in just a few lines.
```
graph = Graph()

graph.add_node(agent)
graph.add_node(summarizer_agent)

graph.add_edge(START, agent)
graph.add_edge(agent, summarizer_agent)
graph.add_edge(summarizer_agent, END)
```

## Run your Graph
You're done! Prompt your agentic architecture.
```
graph.invoke("Hello there!")
```
