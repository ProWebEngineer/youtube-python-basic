def main():
    scores = {"国語": 80, "数学": 75, "英語": 92}

    total = sum(scores.values())
    print(f"合計点: {total}点")
    average = total / len(scores)
    print(f"平均点: {average}点")

if __name__ == "__main__":
    main()