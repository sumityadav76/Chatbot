# Updated Task 1: Realistic Rule-based Chatbot

import datetime

def chatbot():
    print("🤖 Chatbot: Namaste! Main aapka dost PyBot hoon. 'bye' likh ke exit kar sakte ho.")
    while True:
        user_input = input("👤 You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("🤖 PyBot: Hello! Aap kaise ho?")
        elif "kaise ho" in user_input:
            print("🤖 PyBot: Main mast hoon 😄, aap kaise ho?")
        elif "tumhara naam" in user_input or "name" in user_input:
            print("🤖 PyBot: Mera naam PyBot hai, ek chhota sa chatbot jo aapka dost ban sakta hai.")
        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%I:%M %p")
            print(f"🤖 PyBot: Abhi ka time hai {now}.")
        elif "kya kar rahe ho" in user_input:
            print("🤖 PyBot: Bas aap se baat kar raha hoon, aur aapka din better banane ki koshish kar raha hoon.")
        elif "bye" in user_input:
            print("🤖 PyBot: Accha chalo, apna khayal rakhna! 👋")
            break
        else:
            print("🤖 PyBot: Hmm... ye mujhe samajh nahi aaya, par interesting lagta hai!")

if __name__ == "__main__":
    chatbot()
