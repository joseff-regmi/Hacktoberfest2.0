import sys
from execute import printOut
#This is main menu

def Running():
	print ("#================ MAIN MENU ===================#")
	print ("*] 1. Print Primes")
	print ("*] 2. Adivina")
	print ("*] 3. ContadordeVocales2")
	print ("*] 4. ContadorVocales")
	print ("*] 5. ExpRegulares")
	print ("*] 6. HCF")
	print ("*] 7. Obtener Primos")
	print ("*] 8. Palindromo")
	print ("*] 0. Quit")
	print ("#==============================================#")
	choice = input("Choose what do you wanna do (number) : ")

	if choice == '0':
		sys.exit()
	elif choice != None:
	    printOut(choice)

#Running...
Running()