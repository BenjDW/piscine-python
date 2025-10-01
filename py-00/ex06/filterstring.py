import sys
from ft_filter import ft_filter


def main():
    """
    Module main <filterstring>

    the program output a list of words from S,
    that have a length greater than N.
    check all the error , raises exception , call the ft_filter function

    Args:
        none, the two string are taken by sys.argv

    Returns:
        none

    Raises:
        AssertionError: if the number of args is wrong
        or if there are not valid
    """

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
    # comprehension list
    res = [i for i in ft_filter(lambda word: len(word) > n, word)]
    print(res)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
