import ollama
msgs=[
    {
        "role": "system",
        "content": "bahave like a funny ai"
    }
]
while True:
    question = input("Ask the question: ")
    if question.lower() == "exit":
        break
    msgs.append(
        {"role":"user", 
        "content":question})
    response= ollama.chat(
        model="llama3.2:3b",
        messages=msgs
    )
    msgs.append(
        {"role":"assistant", 
        "content":response["message"]["content"]}
    )
    print("AI:",response["message"]["content"])
print("---chat history---\n")
for msg in msgs:
    if msg["role"] == "system":
        continue
    print(msg["role"] + ":", msg["content"])