nums = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
prom = sum(nums) // len(nums)

if prom in nums:
    print(f"El promedio es: {prom}, y está en la lista.")
else:
    print(f"El promedio es: {prom}, y no está en la lista.")