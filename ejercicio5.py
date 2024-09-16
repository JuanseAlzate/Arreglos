nums = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
mayNum = max(nums)
rep = nums.count(mayNum)

if rep == 1:
    print(f"El número mayor es {mayNum}, y está {rep} vez.")
else:
    print(f"El número mayor es {mayNum}, y está {rep} veces.")