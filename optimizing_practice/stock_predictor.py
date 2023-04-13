def greatest_profit(predicted_prices):
    """return the greatest profit that can be made from a single buy transaction 
    followed by a single sell transaction. O(N)"""

    greatest_profit = 0
    lowest_price = predicted_prices[0]
    highest_price = 0
    for price in predicted_prices:
        # if a new lowest price is reset lowest price and highest price
        if price < lowest_price:
            lowest_price = price
            highest_price = price
        # if a new highest price is found, check to see if the profit would be greater than the current greatest profit
        # if it is then it becomes the new greatest profit
        elif price > highest_price:
            highest_price = price
            profit = highest_price - lowest_price
            if profit > greatest_profit:
                greatest_profit = profit
    return greatest_profit

def main():
    predicted_prices = [10, 7, 5, 8, 11, 2, 6]
    print(greatest_profit(predicted_prices))

    predicted_prices2 = [8, 5, 10, 4, 6, 7]
    print(greatest_profit(predicted_prices2))

if __name__ == '__main__':
    main()