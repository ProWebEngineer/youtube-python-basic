def main():
    numbers = [10, 20, 30, 40, 50]
    
    # total = 0
    # for number in numbers:
    #     total += number
    # print("合計:", total)

    total = sum(numbers)
    print("合計:", total)

    average = total / len(numbers)
    print("平均:", average)


if __name__ == "__main__":
    main()