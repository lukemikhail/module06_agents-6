# test_my_assistant.py
# Author: Luke Mikhail

from mock_model import MockModel
from my_assistant import FAQAssistant
from my_tool import FAQS, FAQTool


class SilentModel:
    """A model that returns no answer."""

    def reply(self, instructions, history):
        return None


def make_bot(model=None):
    faq_tool = FAQTool(FAQS)

    if model is None:
        model = MockModel()

    return FAQAssistant(
        "Bayside Helper",
        "You are a helpful store assistant.",
        faq_tool,
        model,
    )


def test_hours_question_returns_store_hours():
    bot = make_bot()
    assert "Monday through Saturday" in bot.respond("What are your hours?")


def test_returns_question_returns_return_policy():
    bot = make_bot()
    assert "30 days" in bot.respond("What is your returns policy?")


def test_shipping_question_returns_shipping_info():
    bot = make_bot()
    assert "3 to 5 business days" in bot.respond("How long does shipping take?")


def test_unknown_question_uses_model():
    bot = make_bot()
    assert "not sure" in bot.respond("Can you repair my tent?")


def test_unknown_question_gets_safe_reply_when_model_returns_none():
    bot = make_bot(SilentModel())
    assert "human employee" in bot.respond("Can you repair my tent?")


def test_respond_records_both_messages():
    bot = make_bot()
    bot.respond("What are your hours?")
    assert len(bot.history) == 2
