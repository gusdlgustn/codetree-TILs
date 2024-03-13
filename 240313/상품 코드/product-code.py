name, code = input().split()

class Product:
    def __init__(self, name="codetree", code=50):
        self.name = name
        self.code = code

pd1 = Product()
pd2 = Product(name, code)

print(f"product {pd1.code} is {pd1.name}")
print(f"product {pd2.code} is {pd2.name}")