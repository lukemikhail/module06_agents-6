# my_assistant.py
# Author: Luke Mikhail


class FAQAssistant:
    """A simple assistant for Bayside Outfitters."""

    def __init__(self, name, instructions, faq_tool, model):
        self.name = name
        self.instructions = instructions
        self.faq_tool = faq_tool
        self.model = model
        self.history = []

    def respond(self, question):
        """Answer a question and save the conversation."""

        self.history.append({"role": "user", "content": question})

        answer = self.faq_tool.find_answer(question)

        if answer is None:
            answer = self.model.reply(self.instructions, self.history)

        if answer is None:
            answer = "I'm not sure about that. I'll connect you with a human employee."

        self.history.append({"role": "assistant", "content": answer})

        return answer
