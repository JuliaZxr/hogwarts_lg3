#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/220 21:00
# @Author  : Yuki


"""
修改work3的计算器测试代码：
1、用fixture的yield代替setup()和teardown()方法，scope参数控制作用域-->
    原来是在class级别的setup()方法中实例化Calculator类：calc = Calculator() ，并在测试类的方法中通过self.calc进行调用 ==
    使用fixture装饰器，在yield之前实例化Calculator类，并通过yield返回实例化的calc供使用，在测试类的方法中通过fixture方法名进行传参使用，方法中的self.calc 需要一并切换成fixture方法名

    这一步在执行测试用例之前完成，即这个fixture方法可以放入conftest.py 文件
2、用fixture参数化 测试用例数据
从.yml文件获取测试用例数据的方法可以放到conftest.py文件中

"""

# 引用
import os

from python_practice.work3_calculator.calculatorCode.calculator import Calculator
import pytest
import allure
import yaml

from python_practice.work4_calculatorFixture.calculatorTestFixture.conftest import get_datas


@pytest.fixture(params=get_datas()[1][0], ids=get_datas()[1][1])
def get_2Datas(request):
    return request.param


@pytest.fixture(params=get_datas()[2][0], ids=get_datas()[2][1])
def get_3Datas(request):
    return request.param


@pytest.fixture(params=get_datas()[3][0], ids=get_datas()[3][1])
def get_4Datas(request):
    return request.param


@pytest.fixture(params=get_datas()[4][0], ids=get_datas()[4][1])
def get_5Datas(request):
    return request.param


@pytest.fixture(params=get_datas()[5][0], ids=get_datas()[5][1])
def get_6Datas(request):
    return request.param


@pytest.fixture(params=get_datas()[6][0], ids=get_datas()[6][1])
def get_7Datas(request):
    return request.param


@pytest.fixture(params=get_datas()[7][0], ids=get_datas()[7][1])
def get_8Datas(request):
    return request.param


@allure.feature("计算器模块")
class TestCalculator:
    # 加法-测试用例参数化

    """
    通过get_datas去文件中读取测试用例
    """

    # @pytest.mark.parametrize("a,b,expected", get_datas()[0], ids=get_datas()[1])
    @pytest.mark.add
    @allure.story("计算器-加法-正确用例")
    def test_add(self, get_calc, get_1Datas):
        print("测试加法-正确用例")
        result = get_calc.add(get_1Datas[0], get_1Datas[1])
        assert result == get_1Datas[2]

    # @pytest.mark.parametrize("a,b,expected", get_datas()[2], ids=get_datas()[3])
    @pytest.mark.add
    @allure.story("计算器-加法-错误用例")
    def test_addMistake(self, get_calc, get_2Datas):
        # calc = Calculator()
        print("测试加法-错误用例")
        result = get_calc.add(get_2Datas[0], get_2Datas[1])
        assert result == get_2Datas[2]

    # 减法-测试用例参数化

    # @pytest.mark.parametrize("a,b,expected", get_datas()[4], ids=get_datas()[5])
    @pytest.mark.subtract
    @allure.story("计算器-减法-正确用例")
    def test_subtract(self, get_calc, get_3Datas):
        # calc = Calculator()
        print("测试减法-正确用例")
        result = round(get_calc.subtract(get_3Datas[0], get_3Datas[1]), 1)
        assert result == get_3Datas[2]

    # @pytest.mark.parametrize("a,b,expected", get_datas()[6], ids=get_datas()[7])
    @pytest.mark.subtract
    @allure.story("计算器-减法-错误用例")
    def test_subtractMistake(self, get_calc, get_4Datas):
        # calc = Calculator()
        print("测试减法-错误用例")
        result = round(get_calc.subtract(get_4Datas[0], get_4Datas[1]), 1)
        assert result == get_4Datas[2]

    # 乘法-测试用例参数化

    # @pytest.mark.parametrize("a,b,expected", get_datas()[8], ids=get_datas()[9])
    @pytest.mark.multiply
    @allure.story("计算器-乘法-正确用例")
    def test_multiply(self, get_calc, get_5Datas):
        # calc = Calculator()
        print("测试乘法-正确用例")
        result = get_calc.multiply(get_5Datas[0], get_5Datas[1])
        assert result == get_5Datas[2]

    # @pytest.mark.parametrize("a,b,expected", get_datas()[10], ids=get_datas()[11])
    @pytest.mark.multiply
    @allure.story("计算器-乘法-错误用例")
    def test_multiplyMistake(self, get_calc, get_6Datas):
        # calc = Calculator()
        print("测试乘法-错误用例")
        result = get_calc.multiply(get_6Datas[0], get_6Datas[1])
        assert result == get_6Datas[2]

    # 除法-测试用例参数化

    # @pytest.mark.parametrize("a,b,expected", get_datas()[12], ids=get_datas()[13])
    @pytest.mark.divide
    @allure.story("计算器-除法-正确用例")
    def test_divide(self, get_calc, get_7Datas):
        # calc = Calculator()
        print("测试除法-正确用例")
        result = round(get_calc.divide(get_7Datas[0], get_7Datas[1]), 1)
        assert result == get_7Datas[2]

    # @pytest.mark.parametrize("a,b,expected", get_datas()[14], ids=get_datas()[15])
    @pytest.mark.divide
    @allure.story("计算器-除法-错误用例")
    def test_divideMistake(self, get_calc, get_8Datas):
        # calc = Calculator()
        try:
            result = round(get_calc.divide(get_8Datas[0], get_8Datas[1]), 1)
            assert result == get_8Datas[2]
        except ZeroDivisionError:
            print("测试除法-异常用例：被除数不能为0")
        else:
            print("测试除法-错误用例")
