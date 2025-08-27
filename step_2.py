from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.save_context({"input": "Hello!"}, {"output": "Hi, how can I help you today?"})
print("Conversation so far:", memory.buffer)
