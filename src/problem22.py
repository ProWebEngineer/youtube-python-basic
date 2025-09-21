def main():
    person = {
        "name": "太郎",
        "age": 20,
        "city": "東京"
    }
    print(person["name"])
    print(person["city"])

    # print(person.get("name"))
    # print(person.get("city"))
    # print(person.get("test", "デフォルト値"))

if __name__ == "__main__":
    main()