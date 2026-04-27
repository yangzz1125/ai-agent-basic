import pytest
from pydantic import ValidationError

from models import ChatRequest, ChatResponse


def test_chat_request_accepts_non_empty_question():
    request = ChatRequest(question="什么是 AI Agent？")

    assert request.question == "什么是 AI Agent？"


def test_chat_request_rejects_empty_question():
    with pytest.raises(ValidationError):
        ChatRequest(question="")


def test_chat_response_stores_answer():
    response = ChatResponse(answer="这是一个模拟回答。")

    assert response.answer == "这是一个模拟回答。"
