def main():
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

if __name__ == "__main__":
    main()