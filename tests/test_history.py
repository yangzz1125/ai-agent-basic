from history import load_chat_records, save_chat_record
from models import ChatRequest, ChatResponse


def test_load_chat_records_returns_empty_list_when_file_missing(tmp_path):
    history_file = tmp_path / "history.json"

    records = load_chat_records(history_file)

    assert records == []


def test_save_chat_record_writes_record(tmp_path):
    history_file = tmp_path / "history.json"
    request = ChatRequest(question="什么是日志？")
    response = ChatResponse(answer="日志用来记录程序运行状态。")

    record = save_chat_record(request, response, history_file)
    records = load_chat_records(history_file)

    assert record.question == "什么是日志？"
    assert len(records) == 1
    assert records[0].answer == "日志用来记录程序运行状态。"
