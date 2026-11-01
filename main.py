print("===power calculator===")
base = int(input("enter a base number:"))
exponent = int(input("enter the power:"))
result = 1
for i in range(1, exponent + 1):
    result = result * base
print(base)
print(exponent)
