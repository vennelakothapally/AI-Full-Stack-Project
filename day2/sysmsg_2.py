import ollama
question= input("Ask the question")
response= ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"you are teaching a 5 years old child.Give the answer in 2-3 lines only"
        },
        {
            "role":"user",
            "content":question
        }
    ]
)
print(response["message"]["content"])