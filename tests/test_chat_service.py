from chat_service import generate_answer
from models import ChatRequest


def test_generate_answer_contains_question():
    request = ChatRequest(question="pytest 是什么？")

    response = generate_answer(request)

    assert "pytest 是什么？" in response.answer
    assert response.answer.startswith("这是一个模拟回答")
