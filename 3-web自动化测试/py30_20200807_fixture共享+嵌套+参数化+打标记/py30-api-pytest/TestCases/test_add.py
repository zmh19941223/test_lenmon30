"""
======================
Author: 柠檬班-小简
Time: 2020/7/20 20:20
Project: day10
Company: 湖南零檬信息技术有限公司
======================
"""
import unittest
from jsonpath import jsonpath

import os
import json

from Common.handle_requests import send_requests
from Common.handle_excel import HandleExcel
from Common.myddt import ddt,data
from Common.handle_path import datas_dir
from Common.my_logger import logger
from Common.handle_db import HandleDB
from Common.handle_data import replace_case_by_regular,EnvData,clear_EnvData_attrs
from Common.handle_extract_data_from_response import extract_data_from_response
import pytest

# 读数据
he = HandleExcel(os.path.join(datas_dir,"api_cases.xlsx"), "加标")
cases = he.read_all_datas()
he.close_file()


@pytest.mark.usefixtures("init_envdata")
class TestAdd:

    @pytest.mark.parametrize("case",cases)
    def test_add(self,case,db):
        # 替换case -
        case = replace_case_by_regular(case)
        # 如果前置sql - 得到结果后，再次替换。
        # 发送请求 - 考虑用例是否都需要token
        if hasattr(EnvData,"token"):
            response = send_requests(case["method"],case["url"],case["request_data"],token=EnvData.token)
        else:
            response = send_requests(case["method"], case["url"], case["request_data"])
        # 如果有提取表达式，提取数据，设置为全局变量。
        if case["extract_data"]:
            extract_data_from_response(case["extract_data"],response.json())
        # 如果有期望结果，则断言

        # 如果有check_sql,数据库较验。
        if case["check_sql"]:
            result = db.select_one_data(case["check_sql"])
            logger.info("数据库查询结果为：")
            logger.info(result)




