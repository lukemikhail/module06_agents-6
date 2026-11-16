from fallback_model import FallbackModel
from keyword_model import KeywordModel


class SilentModel:
    """A model that does not return an answer."""

    def decide(self, instructions, history, tools):
        return None


def test_fallback_uses_keyword_model_when_first_model_returns_none():
    model = FallbackModel(SilentModel(), KeywordModel())
    history = [{"role": "user", "content": "hello"}]

    reply = model.decide("Be friendly.", history, [])

    assert reply == {"text": "Hello! How can I help you today?"}
