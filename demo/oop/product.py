class Product:
    def __init__(self,name):
        self.name = name


p = Product('iPhone 16 Pro')

print(getattr(p, 'name'))
setattr(p, 'price', 100000)

print(p.__dict__)

print(hasattr(p, 'price'))
delattr(p, 'price')
print(hasattr(p, 'price'))






