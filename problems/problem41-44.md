# 第 10 回 Python 基礎問題

**学習ポイント**：UnitTest の基本

---

## **問題 41: unittest の基本**

**課題:**

関数 add(num1, num2) を定義し、2 つの数の和を返すようにしてください。

次に unittest を使って、add(2, 3) が 5 になることをテストしてください。

---

## **問題 42: 複数のテスト**

**課題:**

関数 is_even(num) を定義し、偶数なら True、奇数なら False を返すようにしてください。

次に unittest を使って以下を確認してください。

- is_even(2) → True
- is_even(3) → False

---

## **問題 43: クラスのテスト**

**課題:**

Rectangle クラスを定義し、area() メソッドで面積を返すようにしてください。

次に unittest を使って以下を確認してください。

- Rectangle(3, 4).area() → 12
- Rectangle(5, 6).area() → 30

---

## **問題 44: 例外処理のテスト**

**課題:**

関数 divide(num1, num2) を定義し、num1 ÷ num2 を返すようにしてください。

ただし、0 で割ろうとした場合は ZeroDivisionError を発生させます。

次に unittest を使って「0 で割ったときに ZeroDivisionError が発生すること」をテストしてください。
