# 测试文件
import pytest
import sys
import yaml

sys.path.append('..')
from pythoncode.calc import Calculator


# 定义测试类
class TestCale:
    # 调用被测类
    cal = Calculator()

    @pytest.mark.parametrize('a', yaml.safe_load(open('./number.yml')))
    @pytest.mark.parametrize('b', yaml.safe_load(open('./number.yml')))
    def test_add(self, a, b):
        a = a['a']
        b = b['b']
        try:
            result = a + b
            print(f"\na的值为：{a}")
            print(f'b的值为：{b}')
            print(f'result的值为：{result}')
        except Exception as Exc:
            print(f'\n测试用例异常返回结果为：{Exc}')
            calc_Exc = self.cal.add(a, b)
            print(f'程序异常返回结果为：{calc_Exc}')
            if str(Exc) == str(calc_Exc):
                print('异常检测成功')
                assert True
            else:
                print("异常检测不通过")
                assert False
        else:
            assert result == self.cal.add(a, b)

    @pytest.mark.parametrize('a', yaml.safe_load(open('./number.yml')))
    @pytest.mark.parametrize('b', yaml.safe_load(open('./number.yml')))
    def test_sub(self, a, b):
        a = a['a']
        b = b['b']
        try:
            result = a - b
            print(f'\na的值为：{a}')
            print(f'b的值为：{b}')
            print(f'result的值为{result}')
        except Exception as Exc:
            print(f'\n测试用例异常返回结果为：{Exc}')
            err_Exc = self.cal.sub(a, b)
            print(f'程序异常返回结果为：{err_Exc}')
            if str(Exc) == str(err_Exc):
                print('异常检测成功')
                assert True
            else:
                print('异常检测失败')
                assert False
        else:
            assert result == self.cal.sub(a, b)

    @pytest.mark.parametrize('a', yaml.safe_load(open('./number.yml')))
    @pytest.mark.parametrize('b', yaml.safe_load(open('./number.yml')))
    def test_mul(self, a, b):
        a = a['a']
        b = b['b']
        try:
            result = a * b
            print(f'\na的值为：{a}')
            print(f'b的值为：{b}')
            print(f'result的值为{result}')
        except Exception as Exc:
            print(f'\n测试用例异常返回结果为：{Exc}')
            err_Exc = self.cal.mul(a, b)
            print(f'程序异常返回结果为：{err_Exc}')
            if str(Exc) == str(err_Exc):
                print('异常检测成功')
                assert True
            else:
                print('异常检测失败')
                assert False
        else:
            assert result == self.cal.mul(a, b)

    @pytest.mark.parametrize('a', yaml.safe_load(open('./number.yml')))
    @pytest.mark.parametrize('b', yaml.safe_load(open('./number.yml')))
    def test_div(self, a, b):
        a = a['a']
        b = b['b']
        try:
            result = a / b
            print(f'\na的值为：{a}')
            print(f'b的值为：{b}')
            print(f'result的值为{result}')
        except Exception as Exc:
            print(f'\n测试用例异常返回结果为：{Exc}')
            err_Exc = self.cal.div(a, b)
            print(f'程序异常返回结果为：{err_Exc}')
            if str(Exc) == str(err_Exc):
                print('异常检测成功')
                assert True
            else:
                print('异常检测失败')
                assert False
        else:
            assert result == self.cal.div(a, b)
