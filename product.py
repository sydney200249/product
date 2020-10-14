import os #作業系統模組

product = []
if os.path.isfile('product.txt'):
	print('找到檔案了！')
	#讀取檔案並指定要跳過印出的項目
	with open('product.txt', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			print(name, price)
else:
	print('找不到檔案...')


#請使用者輸入
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