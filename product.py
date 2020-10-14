import os #作業系統模組

#讀取檔案並指定要跳過印出的項目
def read_file(filename):
	product = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name, price])
	return product
#請使用者輸入
def user_input(product):
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		price = int(price)
		product.append([name, price])
	return(product)

#印出所有購買紀錄
def print_product(product):
	for p in product:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, product):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in product:
			f.write(p[0] + ',' + str(p[1]) + '\n')

#集合成主程式
def main():
	filename = 'product.csv'
	if os.path.isfile(filename):
		print('找到檔案了')
		product = read_file(filename)
	else:
		print('找不到檔案')

	product = user_input(product)
	print_product(product)
	write_file('product.csv', product)

#執行
main()
