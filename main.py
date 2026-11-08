# main.py
# Author: Luke Mikhail

from chatbot import SupportChatbot
from ollama_model import OllamaModel
from order_tool import OrderLookup
from stock_tool import StockLookup

ORDERS = {
    "A100": "shipped",
    "A101": "processing",
    "A102": "delivered",
}

STOCK = {
    "rain jacket": 12,
    "day pack": 0,
    "trail hat": 5,
}

INSTRUCTIONS = """You are Sunny, a friendly support assistant for Bayside Outfitters.
Store hours are 10 AM to 7 PM every day.
Customers can return items within 30 days with a receipt.
Shipping takes 3 to 5 business days.
Sale items cannot be returned.

IMPORTANT RULES:
- Only provide facts that are included in these instructions or the conversation.
- Never invent phone numbers, addresses, prices, policies, or other details.
- If you do not know an answer, say you do not have that information.
- Offer to connect the customer with a human when you cannot answer."""

order_tool = OrderLookup(ORDERS)
stock_tool = StockLookup(STOCK)

model = OllamaModel("granite4.1:3b")

bot = SupportChatbot(
    "Sunny",
    INSTRUCTIONS,
    order_tool,
    stock_tool,
    model,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")

while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
