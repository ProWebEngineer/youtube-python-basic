def main():
    try:
        user_input = input("数字を入力してください: ")
        number = int(user_input)
        print(f"入力された数字: {number}")
    except ValueError:
        print("整数を入力してください")


if __name__ == "__main__":
    main()