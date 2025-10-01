from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

"""
tester.py

This script is used to test the functions of the project.
It imports the module(s) and runs sample cases.
"""

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

for elem in tqdm(range(333)):
    sleep(0.005)
    # pass
print()
