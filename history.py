import json
from pathlib import Path

from models import ChatRecord, ChatRequest, ChatResponse


HISTORY_FILE = Path("history.json")


def load_chat_records(history_file: Path = HISTORY_FILE) -> list[ChatRecord]:
    if not history_file.exists():
        return []

    try:
        data = json.loads(history_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    return [ChatRecord.model_validate(item) for item in data]
    # model_validate 是 pydantic v2 的方法，把一个字典数据校验并转换成 Pydantic 模型对象。

def save_chat_record(
    request: ChatRequest,
    response: ChatResponse,
    history_file: Path = HISTORY_FILE,
) -> ChatRecord:
    records = load_chat_records(history_file)
    record = ChatRecord(question=request.question, answer=response.answer)
    records.append(record)

    history_file.write_text(
        json.dumps(
            [item.model_dump(mode="json") for item in records],# model_dump 是 pydantic v2 的方法，把一个 Pydantic 模型对象转换成字典数据。
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    return record
