# my_main.py
# Author: Luke Mikhail

from my_assistant import FAQAssistant
from my_tool import FAQS, FAQTool
from my_toolbox import MyToolbox
from ollama_model import OllamaModel
from pickup_queue import PickupQueue

INSTRUCTIONS = """You are a helpful assistant for Bayside Outfitters.

Bayside Outfitters sells outdoor clothing, jackets, backpacks, and hiking gear.

Store hours are Monday through Saturday, 9 AM to 7 PM.
Standard shipping takes 3 to 5 business days.

You can use tools to answer store questions and check product stock.

Only request a pickup when the customer has provided both the product
and the store location. Pickup requests must wait for staff approval.

Do not make up customer details or store information.
Send complaints and payment disputes to a human employee.
If you do not know an answer, say so and offer human help."""

faq_tool = FAQTool(FAQS)
pickup_queue = PickupQueue()
toolbox = MyToolbox(faq_tool, pickup_queue)
model = OllamaModel("granite4.1:3b")

bot = FAQAssistant(
    "Bayside Helper",
    INSTRUCTIONS,
    faq_tool,
    model,
    toolbox,
)

print("Welcome to Bayside Outfitters! Ask me a question or type quit to exit.")
question = input("You: ")

while question.lower() != "quit":
    print(f"{bot.name}: {bot.respond(question)}")
    question = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")

print("\nStaff review")

for request in pickup_queue.waiting():
    print(
        f"Request {request['number']}: "
        f"{request['item']} for pickup in {request['location']}"
    )
    decision = input("Approve? yes or no: ").strip().lower()

    if decision == "yes":
        print(pickup_queue.approve(request["number"]))
    else:
        print(pickup_queue.reject(request["number"]))
