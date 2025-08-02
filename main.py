from agent_graph import graph
from langchain_core.messages import HumanMessage

query = input("❓ Ask something: ")

print("⚙️ Running AI Agent...")

result = graph.invoke({
    "messages": [HumanMessage(content=query)]
})

print("\n✅ Done!\n")
for msg in result["messages"]:
    if msg.type == "ai":
        print("🤖 Response:", msg.content)
