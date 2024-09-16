def numPrimo(num):
    if num < 2:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True

numsPrimos = [num for num in range(100,300 + 1) if numPrimo(num)][:10]
print(f"Los primeros 10 números primos entre 100 y 300 son: {numsPrimos}.")