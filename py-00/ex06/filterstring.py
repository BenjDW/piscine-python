import sys
from ft_filter import ft_filter

def main():
	if len(sys.argv) != 3:
		raise AssertionError("the arguments are bad")
	
	try:
		string = str(sys.argv[1])
	except ValueError:
		raise AssertionError("the arguments are bad")

	try:
		n = int(sys.argv[2])
	except ValueError:
		raise AssertionError("the arguments are bad")
	
	word = string.split()
	res = [i for i in ft_filter(lambda word: len(word) > n, word)]
	print(res)

if __name__ == "__main__":
	try:
		main()
	except AssertionError as e:
		print(f"AssertionError: {e}")