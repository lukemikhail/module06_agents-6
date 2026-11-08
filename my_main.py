# my_main.py
# Author: Luke Mikhail

from my_assistant import FAQAssistant
from my_tool import FAQS, FAQTool
from ollama_model import OllamaModel

INSTRUCTIONS = """You are a helpful assistant for Bayside Outfitters.
Bayside Outfitters sells outdoor clothing, jackets, backpacks, and hiking gear.
Store hours are Monday through Saturday, 9 AM to 7 PM.
Standard shipping takes 3 to 5 business days.
Only provide facts included in these instructions or the conversation.
If you do not know an answer, say so and offer human help."""

faq_tool = FAQTool(FAQS)
model = OllamaModel("granite4.1:3b")

bot = FAQAssistant(
    "Bayside Helper",
    INSTRUCTIONS,
    faq_tool,
    model,
)

print("Welcome to Bayside Outfitters! Ask me a question or type quit to exit.")

question = input("You: ")

while question.lower() != "quit":
    print(f"{bot.name}: {bot.respond(question)}")
    question = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
