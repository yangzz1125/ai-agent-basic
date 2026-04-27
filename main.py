from pydantic import ValidationError

from chat_service import generate_answer
from config import settings
from history import save_chat_record
from models import ChatRequest
from utils.logger import get_logger


logger = get_logger(__name__)


def main() -> None:
    logger.info("程序启动")
    logger.info("当前环境: %s", settings.APP_ENV or "dev")

    user_input = input("请输入你的问题：").strip()

    try:
        request = ChatRequest(question=user_input)
        logger.info("收到用户问题: %s", request.question)

        response = generate_answer(request)
        logger.info("生成模拟回答")

        save_chat_record(request, response)
        logger.info("问答记录已保存")

        print(f"AI 回复：{response.answer}")
    except ValidationError as error:
        logger.error("问题校验失败: %s", error)
        print("输入错误：问题不能为空。")
    except OSError as error:
        logger.error("保存问答记录失败: %s", error)
        print("保存记录失败，请检查文件权限。")

    logger.info("程序结束")


if __name__ == "__main__":
    main()
