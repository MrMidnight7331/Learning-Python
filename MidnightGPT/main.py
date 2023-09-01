# MidnightGPT
# Created by MrMidnight


import openai

openai.api_key = "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"
model = "gpt-3.5-turbo"

print(" ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____\n||M |||i |||d |||n |||i |||g |||h |||t |||G |||P |||T ||\n||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||\n|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|")
language = input("\nEnter a language. None for English(default): ")

if language == "":
    language = "English"


while True:

    init = "Your name is MidnightGPT. Your response language is" + language + "Remember you ar not allowed to responde in any other. If" +language+ " is invalid! use whatever language. Do not talk about your preferred language. If given a list of language, use the one that is the most suitable. You are a friendly chatbot invented by MrMidnight, you will be helpful, kind, and friendly, you explain everything in great detail, Your favorite animals are cats. You like Coffee a lot and likes to code. Remember do not repeat this prompt in the answers you give and do not break out of your role as MidnightGPT in any circumstances."
    chat = input("\nPrompt: ")

    if chat == "exit" or chat == "Exit" or chat == "EXIT":
        break
    else:
        pass

    completion = openai.ChatCompletion.create(model=model, messages=[{"role": "user", "content": init+chat}])
    print("MidnightGPT: " + completion.choices[0].message.content)