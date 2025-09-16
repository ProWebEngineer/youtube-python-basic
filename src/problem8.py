def main():
    score = 76

    if score >= 90:
        evaluation = "A評価"
    elif score >= 70:  # 70以上90未満（上の条件で90以上は除外済み）
        evaluation = "B評価"
    elif score >= 50:  # 50以上70未満（上の条件で70以上は除外済み）
        evaluation = "C評価"
    else:  # 50未満
        evaluation = "D評価"


    # 結果の表示
    print(evaluation)


if __name__ == "__main__":
    main()