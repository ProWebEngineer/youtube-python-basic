def main():
    max_num = int(input("数字を入力してください: "))
    
    for i in range(1, max_num + 1):
        if i % 3 == 0 and i % 5 == 0:  # 3と5の両方で割り切れる場合
            print("FizzBuzz")
        elif i % 3 == 0:  # 3で割り切れる場合
            print("Fizz")
        elif i % 5 == 0:  # 5で割り切れる場合
            print("Buzz")
        else:  # どちらでも割り切れない場合
            print(i)

if __name__ == "__main__":
    main()