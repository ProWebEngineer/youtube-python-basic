def main():
    price = 1000
    tax = 0.1

    tax_included_price = price * (1 + tax)
    print(f"税込金額: {tax_included_price:.2f}")

if __name__ == "__main__":
    main()