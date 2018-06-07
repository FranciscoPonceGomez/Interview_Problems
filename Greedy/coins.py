def numCoins(cents):
    COINS = [100,50,20,10,5,1]
    res = len(COINS)*[0]
    for i in range(0,len(COINS)):
        res[i] += cents // COINS[i]
        cents %= COINS[i]
    return res

print(numCoins(238))

