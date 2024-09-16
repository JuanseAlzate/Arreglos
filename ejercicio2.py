nums = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
numsPrimos = []

for num in nums:
    if num > 1:
        numPrimo = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                numPrimo = False
                break
        if numPrimo:
            numsPrimos.append(num)

if numsPrimos:
    mayPrimo = max(numsPrimos)
    posPrimo = nums.index(mayPrimo)

    print(f"El número primo mayor es: {mayPrimo}, en la posición: {posPrimo}.")
else:
    print("No hay números primos")