import g4f
from g4f.Provider import (
    Bard,
    ChatBase,
    ChatgptAi,
    OpenaiChat,
    Vercel,
)

def ask_gpt(prompt: str)->str:
    response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    provider=g4f.Provider.ChatgptAi,
    messages=[{"role": "user", "content": prompt}],
    )
    return response

print(ask_gpt(input("Hi, you can ask me any question: ")))