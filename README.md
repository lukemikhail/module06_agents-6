# Bayside Outfitters FAQ Assistant

This project is a support assistant for a fictional outdoor clothing store called Bayside Outfitters. It uses an FAQ tool to answer common questions about store hours, returns, shipping, and products. If the FAQ tool cannot answer a question, the assistant uses a local AI model through Ollama. For example, the AI answered a question about store hours even when the FAQ tool did not recognize the wording. When asked for the company's phone number, the AI correctly said it did not know instead of making one up. The code handles known store information, while the AI helps with other questions.

## How to Run

Run the chatbot:

python3 my_main.py

Run the tests:

pytest -v
