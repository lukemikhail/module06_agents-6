# test_my_assistant.py
# Author: Luke Mikhail

from fake_model import FakeModel
from mock_model import MockModel
from my_assistant import FAQAssistant
from my_tool import FAQS, FAQTool
from my_toolbox import MyToolbox
from pickup_queue import PickupQueue


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


def make_tool_bot(decisions):
    faq_tool = FAQTool(FAQS)
    pickup_queue = PickupQueue()
    toolbox = MyToolbox(faq_tool, pickup_queue)
    model = FakeModel(decisions)
    bot = FAQAssistant(
        "Bayside Helper",
        "You are a helpful store assistant.",
        faq_tool,
        model,
        toolbox,
    )
    return bot, pickup_queue


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


def test_refuses_product_customer_did_not_provide():
    bot, pickup_queue = make_tool_bot(
        [
            {
                "tool": "check_stock",
                "arguments": {"item": "rain jacket"},
            },
            {"text": "Please tell me which product you want checked."},
        ]
    )
    answer = bot.respond("Do you have anything in stock?")
    assert "product you want checked" in answer
    assert "has not provided" in bot.history[1]["content"]
    assert pickup_queue.requests == []


def test_pickup_request_waits_for_staff_approval():
    bot, pickup_queue = make_tool_bot(
        [
            {
                "tool": "request_pickup",
                "arguments": {
                    "item": "rain jacket",
                    "location": "Tampa",
                },
            },
            {"text": "Your pickup request is waiting for staff approval."},
        ]
    )
    answer = bot.respond("I want a rain jacket for pickup in Tampa.")
    assert "waiting for staff approval" in answer
    assert len(pickup_queue.waiting()) == 1
    assert pickup_queue.waiting()[0]["status"] == "waiting"


def test_complaint_is_sent_to_human():
    bot, pickup_queue = make_tool_bot([])
    answer = bot.respond("I want to make a complaint.")
    assert "human employee" in answer
    assert pickup_queue.requests == []
