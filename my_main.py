# my_main.py
# Author: Luke Mikhail

from my_assistant import FAQAssistant
from my_tool import FAQS, FAQTool

faq_tool = FAQTool(FAQS)

bot = FAQAssistant("Bayside Helper", faq_tool)

print("Welcome to Bayside Outfitters! Ask me a question or type quit to exit.")

question = input("You: ")

while question.lower() != "quit":
    print(f"{bot.name}: {bot.respond(question)}")
    question = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
