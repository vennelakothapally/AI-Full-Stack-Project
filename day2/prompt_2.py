import ollama
response= ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"define Ai in 2 lines and  explain three main types of AI in bullet points"
        }
    ]
)
print(response["message"]["content"])