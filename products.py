products = []
while True:
	name = input('請輸入商品明撐: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = [name, price]
	products.append([name, price])
print(products)

