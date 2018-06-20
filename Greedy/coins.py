def numCoins(cents):
    COINS = [100,50,20,10,5,1]
    res = len(COINS)*[0]
    for i in range(0,len(COINS)):
        res[i] += cents // COINS[i]
        cents %= COINS[i]
    return res

def numCoinsDinamyc(cents):
    def aux(cents,index):
        if index == len(COINS)-1:
            return res
        for coin in COINS:
            res[index] += cents // coin
            print(cents%COINS[index])
            with_coin = aux(cents % coin, index+1)
            print(with_coin)
            without_coin = aux(cents,index+1)
            if sum(with_coin) > sum(without_coin):
                res[index] += cents // coin

    COINS = [100,50,20,10,5,1]
    res = len(COINS)*[0]
    return aux(cents,0)


print(numCoinsDinamyc(238))

