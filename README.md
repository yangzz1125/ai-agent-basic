# ai-agent-basic

一个命令行版 AI 问答记录器，用来练习 Python 工程化基础。

这个项目暂时不调用真实大模型 API，而是生成模拟回答。重点是练习项目结构、配置读取、日志、异常处理、Pydantic 数据校验、文件读写和 pytest 测试。

## 功能

- 从 `.env` 读取配置
- 接收用户输入的问题
- 用 Pydantic 校验问题不能为空
- 生成模拟 AI 回复
- 将问答记录保存到 `history.json`
- 使用 pytest 测试核心逻辑

## 安装依赖

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 配置环境变量

创建 `.env` 文件：

```text
API_KEY=replace_with_your_key
BASE_URL=https://example.com
MODEL_NAME=fake-model
APP_ENV=dev
```

`.env` 不要提交到 Git，因为里面可能有真实密钥。

## 运行项目

```powershell
python main.py
```

运行后输入一个问题，程序会返回模拟回答，并保存到 `history.json`。

## 运行测试

```powershell
pytest
```

## 适合练习的知识点

- 命令行运行 Python 程序
- `.env` 和环境变量
- `logging` 日志
- `try/except` 异常处理
- Pydantic 模型校验
- JSON 文件读写
- pytest 单元测试
