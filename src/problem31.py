def main():
    try:
        num1 = int(input("1つ目の整数を入力してください: "))
        num2 = int(input("2つ目の整数を入力してください: "))
        result = num1 / num2
        print(f"結果: {result}")
    except ZeroDivisionError:
        print("0では割れません")
    except ValueError:
        print("整数を入力してください")

    

if __name__ == "__main__":
    main()