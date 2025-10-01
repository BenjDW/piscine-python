import sys


def main():
    """
    Module <SOS>

    only display the morse code of the given string

    Args:
        none, sys.argv is used for taking the string to convert

    Returns:
        none

    Raises:
        AssertionError: if the number of args is not good
        or the character is not contains in the dict

    """
    dictionnary = {
        "A": ".-", "B": "-...",  "C": "-.-.", "D": "-..",
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

    morse = " ".join([dictionnary[c] for c in string])
    print(morse)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
