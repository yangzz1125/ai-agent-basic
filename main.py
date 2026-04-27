from utils.logger import get_logger


logger = get_logger(__name__)


def parse_user_number(text: str) -> int:
    """
    将用户输入的文本转换成整数。
    """
    logger.info("开始解析用户输入")

    number = int(text)

    logger.info("用户输入解析成功")
    return number


def main():
    logger.info("程序启动")

    user_input = input("请输入一个整数：")

    try:
        number = parse_user_number(user_input)
        print(f"你输入的整数是：{number}")

    except ValueError as e:
        logger.error(f"输入解析失败：{e}")
        print("输入错误：请输入合法整数，例如 10、20、100。")

    logger.info("程序结束")


if __name__ == "__main__":
    main()