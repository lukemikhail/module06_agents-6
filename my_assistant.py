# my_assistant.py
# Author: Luke Mikhail


# AI assistance disclosure:
# AI helped generate the initial structure of this class.
# I reviewed the code and understand that:
# - FAQAssistant stores its name, FAQ tool, and conversation history.
# - __init__ sets up the assistant and gives it an empty history.
# - respond saves the user's question in the history.
# - The FAQ tool looks for an answer to the question.
# - If no answer is found, the assistant offers human help.
# - The assistant saves its response and returns it.


class FAQAssistant:
    """A simple assistant for Bayside Outfitters."""

    def __init__(self, name, faq_tool):
        self.name = name
        self.faq_tool = faq_tool
        self.history = []

    def respond(self, question):
        """Answer a question and save the conversation."""
        self.history.append({"role": "user", "content": question})

        answer = self.faq_tool.find_answer(question)

        if answer is None:
            answer = "I'm not sure about that. I'll connect you with a human employee."

        self.history.append({"role": "assistant", "content": answer})
        return answer
