import sys

def morse_code(line):
	dictionnary = { "A": ".-", "B": "-...",  "C": "-.-.", "D": "-..", 
					"E": ".",  "F": "..-.",  "G": "--.", "H": "....",
					"I": "..", "J": ".---", "K": "-.-", "L": ".-..",
					"M": "--", "N": "-.",   "O": "---", "P": ".--.",
					"Q": "--.-", "R": ".-.", "S": "...", "T": "-",
					"U": "..-", "V": "...-", "W": ".--", "X": "-..-",
					"Y": "-.--", "Z": "--..",
					"0": "-----", "1": ".----", "2": "..---", "3": "...--",
					"4": "....-", "5": ".....", "6": "-....", "7": "--...",
					"8": "---..", "9": "----.",
					" ": "/"}
	
	if len(line) == 0:
		raise AssertionError("the arguments are bad")
	string = line.upper()

	if any(c not in dictionnary for c in string):
		raise AssertionError("the arguments are bad")

	morse = " ".join([dictionnary[c] for c in string])
	print(morse)