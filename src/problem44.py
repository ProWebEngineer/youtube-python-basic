def divide(num1, num2):
    """除算を行う関数"""
    if num2 == 0:
        raise ZeroDivisionError("0で割ることはできません")
    return num1 / num2