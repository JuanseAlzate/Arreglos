import math

nums = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
fact = []

for num in nums:
    fact.append(math.factorial(num))

for i in range(10):
    print(f"El factorial de {nums[i]} es {fact[i]}.")