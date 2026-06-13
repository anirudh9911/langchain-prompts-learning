from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are helpful assistant"),
    HumanMessage(content="Tell me about langchain in 3-4 sentences")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)