# fallback_model.py
# Author: Luke Mikhail


class FallbackModel:
    """Try one model first, then use another if the first has no answer."""

    def __init__(self, first_model, second_model):
        """Store the main model and the backup model."""
        self.first_model = first_model
        self.second_model = second_model

    def decide(self, instructions, history, tools):
        """Ask the first model and use the second if it returns None."""
        answer = self.first_model.decide(instructions, history, tools)
        if answer is None:
            return self.second_model.decide(instructions, history, tools)
        return answer
