# my_tool.py
# Author: Luke Mikhail

FAQS = {
    "hours": "We are open Monday through Saturday, 9 AM to 7 PM.",
    "returns": "You can return unused items within 30 days with a receipt.",
    "shipping": "Standard shipping usually takes 3 to 5 business days.",
    "products": "We sell outdoor clothing, jackets, backpacks, and hiking gear.",
}


class FAQTool:
    """Look up answers to common store questions."""

    def __init__(self, faqs):
        self.faqs = faqs

    def find_answer(self, question):
        """Find an FAQ answer based on a keyword."""
        text = question.lower()
        for topic, answer in self.faqs.items():
            if topic in text:
                return answer
        return None
