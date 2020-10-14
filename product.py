#讀取檔案並指定要跳過印出的項目

with open('product.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',')
		print(name, price)

#請使用者輸入
product = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	product.append( [name, price])
print(product)

#印出所有購買紀錄
for p in product:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('product.txt', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')