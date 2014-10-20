import string
import random
correct = False
while not correct:
    alphabet = string.ascii_lowercase.split()[0]
    password = "".join([random.choice(alphabet) for i in range(3)])
    print(password)
    if password == "box":
        correct = True

