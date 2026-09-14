print("================================")
print("       Daily Life Chatbot")
print("================================")

name = input("Bot: What is your name? ")
print("Bot: Nice to meet you,", name)

while True:
    user = input("\n" + name + ": ").lower()

    if "morning" in user:
        print("Bot: Good morning! Start your day with a healthy breakfast.")

    elif "study" in user:
        print("Bot: Try studying for 45 minutes and then take a short break.")

    elif "food" in user or "eat" in user:
        print("Bot: Have a healthy meal and drink enough water.")

    elif "exercise" in user:
        print("Bot: A short walk or some simple exercise is good for your day.")

    elif "free time" in user:
        print("Bot: You can listen to music, watch something, or learn a new skill.")

    elif "sleep" in user:
        print("Bot: Try to sleep on time so you feel fresh tomorrow.")

    elif "tired" in user:
        print("Bot: Take some rest, drink water and relax for a while.")

    elif "bye" in user:
        print("Bot: Bye", name, "! Have a good day.")
        break

    else:
        print("Bot: I am still learning. Try asking about study, food, exercise or sleep.")