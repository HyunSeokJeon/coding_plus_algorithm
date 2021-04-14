
def coin(price):
    coin_list = [500, 100, 50, 1]
    cnt = 0
    for coin in coin_list:
        cnt += price // coin
        price = price % coin

    return cnt

print(coin(4720))