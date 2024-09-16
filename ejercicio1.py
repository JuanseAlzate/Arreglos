nums = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
pos = 0

for i in range(10):
    if nums[i] == max(nums):
        pos = i

print(f"El número mayor de la lista es: {max(nums)}, en la posición: {pos}.")