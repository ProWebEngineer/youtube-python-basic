def main():
    fruits = ["りんご", "みかん", "ぶどう"]

    with open("fruits.txt", "w", encoding="utf-8") as file:
        for fruit in fruits:
            file.write(fruit + "\n")
    print("fruits.txtにフルーツリストを書き込みました。")

    with open("fruits.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
        


if __name__ == "__main__":
    main()