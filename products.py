# 讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 繼續 功能就是跳到下一迴 不會跳出蛔圈
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q': # quit
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    # 第1次簡化 p = [name, price] # 原p = [], 將8,9簡化加入[]之寫法
    # p.append(name) 簡化前
    # p.append(price)簡化前
    products.append([name, price]) #第1次簡化再簡化，
print(products)

# 印出所有購買紀錄
for p in products: # 用for loop來印出商品跟價格(大清單products中的小清單)
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: # 原本是.txt，改成csv是電腦常用檔案且可用excel打開
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')