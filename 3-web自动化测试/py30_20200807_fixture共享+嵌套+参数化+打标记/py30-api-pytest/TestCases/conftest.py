"""
======================
Author: 柠檬班-小简
Time: 2020/8/7 21:26
Project: py30-api-pytest
Company: 湖南零檬信息技术有限公司
======================
"""
import pytest

from Common.my_logger import logger
from Common.handle_data import clear_EnvData_attrs
from Common.handle_db import HandleDB


@pytest.fixture(scope="class")
def init_envdata():
    logger.info("************** 接口 开始测试 ************")
    # 清理 EnvData里设置的属性
    clear_EnvData_attrs()
    yield
    logger.info("************** 接口 结束测试 ************")


@pytest.fixture(scope="session",autouse=True)
def db():
    dbs = HandleDB()
    yield dbs
    dbs.close()
