#猜數字
import random
r = random.randint(1, 100)

while True:
	text = input('Please tpye a number: ')
	text = int(text)
	if text == r:
		print('You got it!')
		break
	elif r < text:
		print('smallar')
	elif r > text:
		print('bigger')

