number = 40
while(True):
	guess = input("Введите число: ")
	if(int(guess) < number):
		print("too little")
	elif(int(guess) > number):
		print("too much")
	else:
		print("Correct")
		break