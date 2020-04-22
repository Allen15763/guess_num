#猜數字
import random
start = input('Please put start number: ')
end = input('Please put end number: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
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

