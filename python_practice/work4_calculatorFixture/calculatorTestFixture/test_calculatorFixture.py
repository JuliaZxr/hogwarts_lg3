#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/220 21:00
# @Author  : Yuki


"""
修改work3的计算器测试代码：
1、用fixture的yield代替setup()和teardown()方法，scope参数控制作用域-->
    原来是在class级别的setup()方法中实例化Calculator类：calc = Calculator() ，并在测试类的方法中通过self.calc进行调用 ==
    使用fixture装饰器，在yield之前实例化Calculator类，并通过yield返回实例化的calc供使用，在测试类的方法中通过fixture方法名进行传参使用，方法中的self.calc 需要一并切换成fixture方法名

    即：①增加get_calc()方法并用fixture装饰，作用域设置为class，返回calc实例
    @pytest.fixture(scope="class")
    def get_calc():
        calc = Calculator()
        print("在类开始时运行一次")
        yield calc
        print("在类结束时运行一次")

    ②具体测试方法中通过参数增加调用fixture装饰的get_calc方法；    def test_add(self, get_calc, a, b, expected)
    ③返回值 从result = self.calc.add(a, b) 变成 result = get_calc.add(a, b)

    ④这一步在执行测试用例之前完成，即这个fixture方法可以放入conftest.py 文件

2、用fixture参数化 测试用例数据 参与fixture带参数传递，return request.param

①因为每一个加减乘除的测试用例方法都需要参数化，所以需要4*2=8个带参数传递的fixture装饰的参数化方法
②在每一个测试用例方法的参数中加上对应参数化的方法名，eg：get_addData，参数化方法中具体某一个值可以用[x]下标来表示 eg：get_addData[0]
③从.yml文件获取测试用例数据的get_datas方法 和 8个参数化方法 可以放到conftest.py文件中

"""
# 引用
import pytest
import allure


@allure.feature("计算器模块")
class TestCalculator:
    # 加法-测试用例参数化
    # 因为使用带参数的fixture装饰方法来参数化，所以在每一个测试用例方法的参数中加上对应参数化的方法名，eg：get_addData，参数化方法中具体某一个值可以用[x]下标来表示
    @pytest.mark.run(order=1)
    @pytest.mark.add
    @allure.story("计算器-加法-正确用例")
    def test_add(self, get_calc, get_addData):
        print("测试加法-正确用例")
        result = get_calc.add(get_addData[0], get_addData[1])
        assert result == get_addData[2]

    @pytest.mark.run(order=2)
    @pytest.mark.add
    @allure.story("计算器-加法-错误用例")
    def test_addMistake(self, get_calc, get_addMistakeData):
        # calc = Calculator()
        print("测试加法-错误用例")
        result = get_calc.add(get_addMistakeData[0], get_addMistakeData[1])
        assert result == get_addMistakeData[2]

    # 除法-测试用例参数化
    @pytest.mark.run(order=7)
    @pytest.mark.divide
    @allure.story("计算器-除法-正确用例")
    def test_divide(self, get_calc, get_divideData):
        # calc = Calculator()
        print("测试除法-正确用例")
        result = round(get_calc.divide(get_divideData[0], get_divideData[1]), 1)
        assert result == get_divideData[2]

    @pytest.mark.run(order=8)
    @pytest.mark.divide
    @allure.story("计算器-除法-错误用例")
    def test_divideMistake(self, get_calc, get_divideMistakeData):
        # calc = Calculator()
        try:
            result = round(get_calc.divide(get_divideMistakeData[0], get_divideMistakeData[1]), 1)
            assert result == get_divideMistakeData[2]
        except ZeroDivisionError:
            print("测试除法-异常用例：被除数不能为0")
        else:
            print("测试除法-错误用例")

    # 减法-测试用例参数化

    @pytest.mark.run(order=3)
    @pytest.mark.subtract
    @allure.story("计算器-减法-正确用例")
    def test_subtract(self, get_calc, get_subtractData):
        # calc = Calculator()
        print("测试减法-正确用例")
        result = round(get_calc.subtract(get_subtractData[0], get_subtractData[1]), 1)
        assert result == get_subtractData[2]

    @pytest.mark.run(order=4)
    @pytest.mark.subtract
    @allure.story("计算器-减法-错误用例")
    def test_subtractMistake(self, get_calc, get_subtractMistakeData):
        # calc = Calculator()
        print("测试减法-错误用例")
        result = round(get_calc.subtract(get_subtractMistakeData[0], get_subtractMistakeData[1]), 1)
        assert result == get_subtractMistakeData[2]

    # 乘法-测试用例参数化

    @pytest.mark.run(order=5)
    @pytest.mark.multiply
    @allure.story("计算器-乘法-正确用例")
    def test_multiply(self, get_calc, get_multiplyData):
        # calc = Calculator()
        print("测试乘法-正确用例")
        result = get_calc.multiply(get_multiplyData[0], get_multiplyData[1])
        assert result == get_multiplyData[2]

    @pytest.mark.run(order=6)
    @pytest.mark.multiply
    @allure.story("计算器-乘法-错误用例")
    def test_multiplyMistake(self, get_calc, get_multiplyMistakeData):
        # calc = Calculator()
        print("测试乘法-错误用例")
        result = get_calc.multiply(get_multiplyMistakeData[0], get_multiplyMistakeData[1])
        assert result == get_multiplyMistakeData[2]

