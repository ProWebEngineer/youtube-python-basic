def main():
    person = {"name": "太郎", "age": 20}

    person["city"] = "大阪"
    person["age"] = 21

    print(person)

    # person.update({"city": "大阪", "age": 21})
    # print(person)

    # person |= {"city": "大阪", "age": 21}
    # print(person)

    # new_person = person | {"city": "大阪", "age": 21}
    # print(new_person)
    # print(person)


if __name__ == "__main__":
    main()