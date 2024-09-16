nums = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]

for num in nums:
    print(f"Números entre 1 y {num}:")
    for i in range(1, num + 1):
        print(i, end=" ")
    print("\n")