def main():
    try:
        user_input = input("数字を入力してください: ")
        number = int(user_input)
    except ValueError:
        print("整数を入力してください")
    else:
        # 正常に入力できた場合のみ実行される
        result = number * 2
        print(f"結果: {result}")
    finally:
        print("プログラムを終了します")

if __name__ == "__main__":
    main()