def main():
    try:
        result = 10 / 0
        print(result)
    except ZeroDivisionError:
        print("エラーが発生しました")

if __name__ == "__main__":
    main()