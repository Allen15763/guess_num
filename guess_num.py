#猜數字
import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	text = input('Please tpye a number: ')
	text = int(text)
	if text == r:
		print('You got it!')
		print('This is', count, 'times')
		break
	elif r < text:
		print('smallar')
	elif r > text:
		print('bigger')
	print('This is', count, 'times')

