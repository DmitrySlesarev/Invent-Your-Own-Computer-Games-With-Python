import random
print('Am gonna flip coin 1K times. Guess the amount of times of heads. Enter to start!')
input()
flips = 0
heads = 0
while flips < 1000:
	if random.randint(0,1) == 1:
		heads += 1
	flips += 1

	if flips == 900:
		print('900 flips and heads come ' + str(heads) + ' times.')
	if flips == 100:
		print('100 flips and heads come ' + str(heads) + ' times.')
	if flips == 500:
		print('You\'re on the halfway and heads come ' + str(heads) + ' times.')

		print()
		print('1K of flips has ' + str(heads) + ' times.')
		print('How close were you?')