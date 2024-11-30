import g4f

g4f.debug.logging = True  
g4f.debug.version_check = False  
#print(g4f.Provider.Bing.params)  

def ask_gpt(prompt: str)->str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.You,
        messages=[{"role": "user", "content": prompt}],
    )
    return response
question = input("Hi, you can ask me any question: ")
while question != "stop":
    print(ask_gpt(question))
    question = input("waiting next prompt: ")