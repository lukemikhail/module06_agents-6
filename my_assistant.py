# my_assistant.py
# Author: Luke Mikhail

HANDOFF_WORDS = ["complaint", "chargeback", "payment dispute"]
MAX_TOOL_ROUNDS = 3


class FAQAssistant:
    """A simple assistant for Bayside Outfitters."""

    def __init__(self, name, instructions, faq_tool, model, toolbox=None):
        self.name = name
        self.instructions = instructions
        self.faq_tool = faq_tool
        self.model = model
        self.toolbox = toolbox
        self.history = []

    def respond(self, question):
        """Answer a question and save the conversation."""
        self.history.append({"role": "user", "content": question})

        if self.needs_human(question.lower()):
            answer = "I'll connect you with a human employee for help."
        elif self.toolbox is not None:
            answer = self.model_reply()
        else:
            answer = self.faq_tool.find_answer(question)
            if answer is None:
                answer = self.model.reply(self.instructions, self.history)
            if answer is None:
                answer = (
                    "I'm not sure about that. I'll connect you with a human employee."
                )

        self.history.append({"role": "assistant", "content": answer})
        return answer

    def needs_human(self, text):
        """Check whether the customer needs help from a person."""
        return any(word in text for word in HANDOFF_WORDS)

    def model_reply(self):
        """Let the model answer or request tools, with a limited tool loop."""
        rounds = 0

        while rounds < MAX_TOOL_ROUNDS:
            decision = self.model.decide(
                self.instructions,
                self.history,
                self.toolbox.tool_list(),
            )

            if decision is None:
                return (
                    "I'm not sure about that. I'll connect you with a human employee."
                )

            if "text" in decision:
                return decision["text"]

            name = decision["tool"]
            arguments = decision["arguments"]
            result = self.toolbox.run(name, arguments, self.history)

            self.history.append(
                {
                    "role": "tool",
                    "tool_name": name,
                    "arguments": arguments,
                    "content": result,
                }
            )
            rounds += 1

        return (
            "I couldn't complete that request. I'll connect you with a human employee."
        )
