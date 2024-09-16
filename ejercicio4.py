nums = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
pos = [i for i, num in enumerate(nums) if num % 10 == 4]
print (f"Los números terminados en 4 están en las posiciones: {pos}.")