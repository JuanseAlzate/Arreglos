def sd(num):
    return sum(int(digito) for digito in str(num))

nums = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
sdm = max(nums, key=sd)
pos = nums.index(sdm)

print(f"El número con la mayor suma de sus dígitos es {sdm} y está en la posición {pos}")