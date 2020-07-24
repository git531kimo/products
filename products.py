products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q': # quit
        break
    price = input('請輸入商品價格: ')
    # 第1次簡化 p = [name, price] # 原p = [], 將8,9簡化加入[]之寫法
    # p.append(name) 簡化前
    # p.append(price)簡化前
    products.append([name, price]) #第1次簡化再簡化，
print(products)