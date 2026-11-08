# echo_model.py
# Author: Luke Mikhail


class EchoModel:
    # This class acts as a simple model for testing the chatbot.

    def reply(self, instructions, history):
        # Get the most recent message from the conversation.
        last_message = history[-1]["content"]

        # Return the message with "You said:" in front of it.
        return "You said: " + last_message
