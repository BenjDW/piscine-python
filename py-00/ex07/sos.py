import sys

def main():
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
	
	if len(sys.argv) != 2:
		raise AssertionError("the arguments are bad")
	string = sys.argv[1].upper()

	if any(c not in dictionnary for c in string):
		raise AssertionError("the arguments are bad")

	# for c in string:
	# 	if c not in dictionnary:
	# 		raise AssertionError("the arguments are bad")

	morse = " ".join([dictionnary[c] for c in string])
	print(morse)

if __name__ == "__main__":
	try:
		main()
	except AssertionError as e:
		print(f"AssertionError: {e}")