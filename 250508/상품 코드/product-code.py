product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.

class product:
    def __init__(self, product_name = '', product_code = 0): 
        self.name = product_name
        self.code = product_code

store_stock1 = product(product_name = 'codetree',product_code = 50)
store_stock2 = product(product_name,product_code)
print(f'product {store_stock1.code} is {store_stock1.name}')
print(f'product {store_stock2.code} is {store_stock2.name}')
