"""Winnie's solution in her main"""
import random
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
def robot_name():
    letters = random.choices(alphabet,k=2)
    digits = random.choices(numbers,k=3)
    name = ''.join(letters + digits)
    return name

print(robot_name())
"""ends here"""