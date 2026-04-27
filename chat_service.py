from models import ChatRequest, ChatResponse


def generate_answer(request: ChatRequest) -> ChatResponse:
    answer = f"这是一个模拟回答：你刚才问的是「{request.question}」。"
    return ChatResponse(answer=answer)
