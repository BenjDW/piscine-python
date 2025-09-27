import sys

def main():
	string = ""
	if len(sys.argv) > 2:
		raise AssertionError("more than one argument is provided")
	elif len(sys.argv) == 2:
		string = sys.argv[1]
	else:
		string = "ma phrase est préfaite, c'est beau la vie"
	
	upper = lower = digit = space = other = c = 0

	for c in string:
		if c.isupper():
			upper += 1
		elif c.islower():
			lower += 1
		elif c.isdigit():
			digit += 1
		elif c.isspace():
			space += 1
		else:
			other += 1
	
	print(f"The text contains {len(string)} characters:")
	print(f"{upper} upper letters")
	print(f"{lower} lower letters")
	print(f"{other} punctuation marks")
	print(f"{space} spaces")
	print(f"{digit} digits")

if __name__ == "__main__":
	try:
		main()
	except AssertionError as e:
		print(f"AssertionError: {e}")
	# __doc__