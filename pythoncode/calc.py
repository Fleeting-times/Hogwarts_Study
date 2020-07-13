# 实现计算器
# 被测文件

class Calculator:
    # 加法
    def add(self, a, b):
        try:
            result = a + b
        except Exception as Exc:
            return Exc
        else:
            return result

    # 减法
    def sub(self, a, b):
        try:
            result = a - b
        except Exception as Exc:
            return Exc
        else:
            return result

    # 乘法
    def mul(self, a, b):
        try:
            result = a * b
        except Exception as Exc:
            return Exc
        else:
            return result

    # 出除法
    def div(self, a, b):
        try:
            result = a / b
        except Exception as Exc:
            return Exc
        else:
            return result


if __name__ == '__main__':
    a = 1
    b = 'a'
    cal = Calculator()
    res = cal.add(a, b)
    print(res)
    if str(res) == "unsupported operand type(s) for +: 'int' and 'str'":
        print('输入字符类型错误')
    else:
        print("非字符类型错误")
