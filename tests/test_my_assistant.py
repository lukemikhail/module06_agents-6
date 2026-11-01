# test_my_assistant.py
# Author: Luke Mikhail

from my_assistant import FAQAssistant
from my_tool import FAQS, FAQTool


def make_bot():
    faq_tool = FAQTool(FAQS)
    return FAQAssistant("Bayside Helper", faq_tool)


def test_hours_question_returns_store_hours():
    bot = make_bot()
    assert "Monday through Saturday" in bot.respond("What are your hours?")


def test_returns_question_returns_return_policy():
    bot = make_bot()
    assert "30 days" in bot.respond("What is your returns policy?")


def test_shipping_question_returns_shipping_info():
    bot = make_bot()
    assert "3 to 5 business days" in bot.respond("How long does shipping take?")


def test_unknown_question_offers_human_help():
    bot = make_bot()
    assert "human employee" in bot.respond("Can you repair my tent?")


def test_respond_records_both_messages():
    bot = make_bot()
    bot.respond("What are your hours?")
    assert len(bot.history) == 2
