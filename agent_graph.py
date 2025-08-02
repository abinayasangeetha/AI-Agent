from langgraph.graph import StateGraph
from typing import TypedDict
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda
import os

# Setup Groq API
os.environ["GROQ_API_KEY"] = "gsk_......A"  # Replace with your real key

llm = ChatGroq(
    temperature=0,
    model_name="llama3-8b-8192",
    api_key=os.environ["GROQ_API_KEY"]
)

# State definition
class AgentState(TypedDict):
    messages: list

# Agent function
def agent_node(state: AgentState) -> AgentState:
    messages = state["messages"]
    response = llm.invoke(messages)
    messages.append(response)
    return {"messages": messages}

# Stop when last message is from AI
def should_continue(state: AgentState) -> bool:
    return not isinstance(state["messages"][-1], AIMessage)

# Build the graph
workflow = StateGraph(AgentState)
workflow.add_node("agent", RunnableLambda(agent_node))
workflow.set_entry_point("agent")

workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        True: "agent",   # keep looping
        False: "end",    # go to end
    }
)

workflow.add_node("end", lambda x: x)  # dummy end node

# Compile the graph
graph = workflow.compile()

