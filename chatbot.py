import openai

openai.api_key = "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"

chat_history = [
    {"role": "system", "content": "Hello user! How may i help?"},
    {"role": "user", "content": "Which team won the IPL 2018"}
]

while(True):
    response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=chat_history )
    reply = response.choices[0].message.content
    print("System: ", reply)
    user_mes = input("user: ")
    if(user_mes == "done"):
        break
    user_message = {"role":"user", "content":user_mes}
    chat_history.append(user_message)



