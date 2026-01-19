from langchain_core.messages import HumanMessage
from agent.graph import react_graph

config = {"configurable": {"thread_id": "user-session-1"}} 

print("Job Helper Agent (type 'quit' to exit)")            
print("-" * 40) 

# chat loop
while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() in ["quit", "exit"]:
        break

    if not user_input:
        continue

    result = react_graph.invoke(
        {"messages": [HumanMessage(content=user_input)]},
        config=config
    )

    print(f"\nAssistant: {result['messages'][-1].content}")