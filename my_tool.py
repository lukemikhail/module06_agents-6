# my_tool.py
# Author: Luke Mikhail

FAQS = {
    "hours": "We are open Monday through Saturday, 9 AM to 7 PM.",
    "returns": "You can return unused items within 30 days with a receipt.",
    "shipping": "Standard shipping usually takes 3 to 5 business days.",
    "products": "We sell outdoor clothing, jackets, backpacks, and hiking gear.",
}


class FAQTool:
    """Look up store information and product stock."""

    def __init__(self, faqs, stock=None):
        """Store the FAQ information and product stock."""
        self.faqs = faqs
        if stock is None:
            stock = {
                "rain jacket": 12,
                "day pack": 0,
                "trail hat": 5,
            }
        self.stock = stock

    def find_answer(self, question):
        """Find an FAQ answer based on a keyword."""
        text = question.lower()
        for topic, answer in self.faqs.items():
            if topic in text:
                return answer
        return None

    def check_stock(self, item):
        """Check how many of an item are available.

        Args:
            item: The product name, such as rain jacket.
        """
        item = item.lower().strip()
        if item not in self.stock:
            return f"We don't have stock information for {item}."
        quantity = self.stock[item]
        if quantity == 0:
            return f"The {item} is currently out of stock."
        return f"We have {quantity} {item}(s) in stock."
