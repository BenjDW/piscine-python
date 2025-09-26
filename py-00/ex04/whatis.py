import sys

def main():
    if len(sys.argv) == 1:
        return ()
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    arg = sys.argv[1]

    try:
        n = int(arg)
    except ValueError:
        raise AssertionError("argument is not an integer")

    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
	try:
		main()
	except AssertionError as e:
		print(f"AssertionError: {e}")
        
