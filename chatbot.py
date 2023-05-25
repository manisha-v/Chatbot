import openai

openai.api_key = "OPENAI_API_KEY"

chat_history = [
    {"role": "system", "content": "Hello user! How may I help?"},
    {"role": "user", "content": "Which team won the IPL 2018"}
]

for mes in chat_history:
    print(mes["role"],": ",mes["content"])

while(True):
    response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=chat_history )
    reply = response.choices[0].message.content
    print("system: ", reply)
    user_mes = input("user: ")
    if(user_mes == "bye"): # ends when user says bye
        break
    user_message = {"role":"user", "content":user_mes}
    chat_history.append(user_message)
