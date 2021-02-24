from datetime import datetime
from flask import Flask


def get_current_time() -> dict:
    return {'current_time': datetime.now()}


def init_app(app: Flask) -> None:
    # 全局模板上下文变量
    app.context_processor(get_current_time)
