x = input('你有沒有開過車?')
y = input('你幾歲?')
y = int(y)
if x == '有':
	if y >= 18:
		print('你好棒!')
	else:
		print('未成年還敢開車阿')
else:
	if y < 18:
		print('嫩!')
	else:
		print('是要幾歲才開車')	