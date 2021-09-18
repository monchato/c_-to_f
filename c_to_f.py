c = input('請輸入攝氏溫度:')
c = float(c)

f = c * 9 / 5 + 32
print('華氏溫度為:', f)

if f > 100:
	print('也太熱了吧被烤焦')