def calc_total(num1: int, num2: int) -> int:
    """
    2つの整数の合計を計算して返す関数
    Args:
        num1 (int): 1つ目の整数
        num2 (int): 2つ目の整数
    Returns:
        int: 2つの整数の合計
    """
    return num1 + num2


def main():
    result = calc_total(5, 10)
    print(f"合計は {result} です")
    

if __name__ == "__main__":
    main()