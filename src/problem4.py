def main():
    item1 = "りんご"
    price1 = 120
    qty1 = 2

    item2 = "みかん"
    price2 = 80
    qty2 = 5

    tax_rate = 0.1  # 消費税率10%

    subtotal1 = price1 * qty1
    subtotal2 = price2 * qty2

    subtotal = subtotal1 + subtotal2
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount

    print("---- レシート ----")
    print(f"{item1} {qty1}個 x {price1}円 = {subtotal1}円")
    print(f"{item2} {qty2}個 x {price2}円 = {subtotal2}円")
    print(f"小計: {subtotal}円")
    print(f"消費税({tax_rate*100:.0f}%): {tax_amount:.0f}円")
    print(f"合計: {total:.0f}円")
    print("------------------")

if __name__ == "__main__":
    main()