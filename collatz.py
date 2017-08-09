# coding:utf-8

def collatz(number):
	if number % 2 == 0: #偶数の場合
		return number / 2
	else: #奇数の場合
		return 3 * number + 1


print('整数を入力してください')
input_number = input()

while True:
	try:
		input_number = int(input_number)
		
		if input_number == 1:
			break
		else:
			input_number = collatz(input_number)
			print(input_number)
	
	except ValueError:
		print('整数以外の数字が記入されました。整数を記入してください')
		input_number = input()