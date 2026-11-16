# my_toolbox.py
# Author: Luke Mikhail


class MyToolbox:
    """Check every request before allowing a tool to run."""

    def __init__(self, faq_tool, pickup_queue):
        """Store the FAQ tool and pickup approval queue."""
        self.faq_tool = faq_tool
        self.pickup_queue = pickup_queue

    def tool_list(self):
        """Return the tools the assistant is allowed to use."""
        return [
            {
                "type": "function",
                "function": {
                    "name": "find_answer",
                    "description": "Look up store information.",
                    "parameters": {
                        "type": "object",
                        "required": ["question"],
                        "properties": {"question": {"type": "string"}},
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "check_stock",
                    "description": "Check product availability.",
                    "parameters": {
                        "type": "object",
                        "required": ["item"],
                        "properties": {"item": {"type": "string"}},
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "request_pickup",
                    "description": "Request an in-store pickup for staff approval.",
                    "parameters": {
                        "type": "object",
                        "required": ["item", "location"],
                        "properties": {
                            "item": {"type": "string"},
                            "location": {"type": "string"},
                        },
                    },
                },
            },
        ]

    def customer_said(self, history, text):
        """Check whether the customer actually provided a detail."""
        for message in history:
            if message["role"] == "user" and text.lower() in message["content"].lower():
                return True
        return False

    def run(self, name, arguments, history):
        """Validate a tool request before running it."""
        if name == "find_answer":
            question = str(arguments.get("question", "")).strip()
            if not question:
                return "Please ask the customer what they want to know."
            answer = self.faq_tool.find_answer(question)
            if answer is None:
                return "I don't have an answer to that question."
            return answer

        if name == "check_stock":
            item = str(arguments.get("item", "")).strip().lower()

            if not item:
                return "Please ask the customer which product they mean."

            if not self.customer_said(history, item):
                return (
                    "The customer has not provided that product name. Ask them first."
                )

            return self.faq_tool.check_stock(item)

        if name == "request_pickup":
            item = str(arguments.get("item", "")).strip().lower()
            location = str(arguments.get("location", "")).strip()

            if not item or not location:
                return "The product and pickup location are both required."

            if not self.customer_said(history, item):
                return (
                    "The customer has not provided that product name. Ask them first."
                )

            if not self.customer_said(history, location):
                return "The customer has not provided that pickup location. Ask them first."

            if item not in self.faq_tool.stock:
                return "That product is not in our stock list."

            if self.faq_tool.stock[item] <= 0:
                return f"The {item} is out of stock, so a pickup request cannot be submitted."

            return self.pickup_queue.request_pickup(item, location)

        return f"There is no tool named {name}."
