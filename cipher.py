#crypto code
SYMBOLS = "АБВГДЕЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеежзийклмнопрестфхцчщъыьэюя"
MAX_KEY_SIZe = len(SYMBOLS)

def getMode():
		while True:
				print("You want to encrypt, decrypt or hack your text?")
				mode = input().lower()
				if mode in ['encrypt', 'e', 'decrypt', 'hack', 'h']:
					return mode
				else:
					print("Enter 'encrypt', 'decrypt' or 'hack' accordingly.")

def getMessage():
	print('Input text:')
	return input()

def getKey()
	key = 0
	while True:
		print("Enter key (1-%s" % (MAX_KEY_SIZe))
		key = int(input())
		if (key >= 1 and key <= MAX_KEY_SIZe):
			return key

def getTranslatedMessage(mode, message, key):
	if mode[0] == 'p':
		key = -key
	translated = " "

	for symbol in message:
			symbolIndex = SYMBOLS.find(symbol)
			if symbolIndex == -1: # The symbol hasn't been found in SYMBOLS.
				# Just add this symbol without changes
				translated += symbol
			else:
				# Encrypt or decript
				symbolIndex += key

				if symbolIndex >= len(SYMBOLS)
					symbolIndex -= len(SYMBOLS)
				elif symbolIndex < 0:
					symbolIndex += len(SYMBOLS)

				translated += SYMBOLS[symbolIndex]
	return translated

mode = getMode()
message = getMessage()
if mode[0] != 'h':
	key = getKey()
print("Encrypted text:")
if mode[0] != 'h':
	print(getTranslatedMessage(mode, message, key))
else:
	for key in range(1, MAX_KEY_SIZE + 1):
		print(key, getTranslatedMessage('encrypt'), message, key)
