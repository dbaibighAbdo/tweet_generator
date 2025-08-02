from langgraph.graph import MessagesState, START, END
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.types import interrupt

from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
from chains import generation_chain, reflection_chain

load_dotenv()


def generator(state: MessagesState) -> MessagesState:
    
    response = generation_chain.invoke({
        "messages": state["messages"]})
    return {"messages": [AIMessage(content=response.content)]}



def reflector(state: MessagesState) -> MessagesState:
    response = reflection_chain.invoke({
        "messages": state["messages"]})
    return {"messages": [HumanMessage(content=response.content)]}



def router(state: MessagesState):
    if len(state["messages"]) > 4:
        return END
    return "reflector"



memory = MemorySaver()
builder = StateGraph(MessagesState)

builder.add_node("generator", generator)
builder.add_node("reflector", reflector)

builder.add_edge(START, "generator")
builder.add_conditional_edges("generator", router)
builder.add_edge("reflector", "generator")

graph = builder.compile(checkpointer=memory)



