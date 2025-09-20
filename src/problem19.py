def main():
    fruits = ["りんご", "みかん"]

    fruits.append("ぶどう")
    print(fruits)

    # fruits.insert(1, "もも")
    # print(fruits)

    # fruits += ["バナナ", "メロン"]
    # print(fruits)

    fruits.remove("みかん")
    print(fruits)

    # fruits.pop(1)
    # print(fruits)

if __name__ == "__main__":
    main()