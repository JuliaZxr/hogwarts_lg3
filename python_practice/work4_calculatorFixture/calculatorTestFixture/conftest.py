#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 23:39
# @Author  : Yuki
import os
from typing import List

import pytest
import yaml

from python_practice.work4_calculatorFixture.calculatorCodeFixture.calculatorCode import Calculator


# 中文编码
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# 实例化被测试的计算机类
@pytest.fixture(scope="class")
def get_calc():
    print("\n-开始计算-")
    calc = Calculator()
    yield calc
    print("-结束计算-")


"""
通过get_datas去文件中读取测试用例
"""
# 从.yml文件中读取测试数据
def get_datas():
    # os.path.dirname(__file__) 代表当前这个文件的路径
    mydatapath = os.path.dirname(__file__) + "./data/calc.yml"
    with open(mydatapath, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        add_mydatas = datas["add"]["mydatas"]
        add_myids = datas["add"]["myids"]
        addMistake_mydatas = datas["addMistake"]["mydatas"]
        addMistake_myids = datas["addMistake"]["myids"]

        subtract_mydatas = datas["subtract"]["mydatas"]
        asubtract_myids = datas["subtract"]["myids"]
        subtractMistake_mydatas = datas["subtractMistake"]["mydatas"]
        subtractMistake_myids = datas["subtractMistake"]["myids"]

        multiply_mydatas = datas["multiply"]["mydatas"]
        multiply_myids = datas["multiply"]["myids"]
        multiplyMistake_mydatas = datas["multiplyMistake"]["mydatas"]
        multiplyMistake_myids = datas["multiplyMistake"]["myids"]

        divide_mydatas = datas["divide"]["mydatas"]
        divide_myids = datas["divide"]["myids"]
        divideMistake_mydatas = datas["divideMistake"]["mydatas"]
        mdivideMistake_myids = datas["divideMistake"]["myids"]

    return [[add_mydatas, add_myids],
            [addMistake_mydatas, addMistake_myids],
            [subtract_mydatas, asubtract_myids],
            [subtractMistake_mydatas, subtractMistake_myids],
            [multiply_mydatas, multiply_myids],
            [multiplyMistake_mydatas, multiplyMistake_myids],
            [divide_mydatas, divide_myids],
            [divideMistake_mydatas, mdivideMistake_myids]]


# 使用带参数传递的fixture装饰方法 去参数化每一个加减乘除方法
@pytest.fixture(params=get_datas()[0][0], ids=get_datas()[0][1])
def get_addData(request):
    return request.param

@pytest.fixture(params=get_datas()[1][0], ids=get_datas()[1][1])
def get_addMistakeData(request):
    return request.param


@pytest.fixture(params=get_datas()[2][0], ids=get_datas()[2][1])
def get_subtractData(request):
    return request.param


@pytest.fixture(params=get_datas()[3][0], ids=get_datas()[3][1])
def get_subtractMistakeData(request):
    return request.param


@pytest.fixture(params=get_datas()[4][0], ids=get_datas()[4][1])
def get_multiplyData(request):
    return request.param


@pytest.fixture(params=get_datas()[5][0], ids=get_datas()[5][1])
def get_multiplyMistakeData(request):
    return request.param


@pytest.fixture(params=get_datas()[6][0], ids=get_datas()[6][1])
def get_divideData(request):
    return request.param


@pytest.fixture(params=get_datas()[7][0], ids=get_datas()[7][1])
def get_divideMistakeData(request):
    return request.param
