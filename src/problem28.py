def calc_total_price(price: int, quantity: int) -> int:
    """
    商品の価格と数量から合計金額を計算して返す関数
    Args:
        price (int): 商品の価格
        quantity (int): 商品の数量
    Returns:
        int: 合計金額
    """
    return price * quantity
    
    

def main():
    total = calc_total_price(150, 3)
    print(total)
    

if __name__ == "__main__":
    main()