def main():
    num1 = 12
    num2 = 20
    num3 = 15

    if num1 >= num2 and num1 >= num3:
        max_value = num1
    elif num2 >= num1 and num2 >= num3:
        max_value = num2
    else:
        max_value = num3

    # max_value = max(num1, num2, num3)

    print(f"最大値は {max_value} です")


if __name__ == "__main__":
    main()