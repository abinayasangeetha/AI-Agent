from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    model_name="llama3-8b-8192", 
    api_key="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"
)

response = llm.invoke("Hello, who are you?")
print(response.content)
