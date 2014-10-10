#Password Generator
#Jack Humphreys

import random
pass_length = int(input("Please enter length of your password: "))
for count in range(pass_length):
    ran_choice1 = random.randint(48,57)
    ran_choice2 = random.randint(65,90)
    ran_choice3 = random.randint(97,122)
    ran_list = [ran_choice1,ran_choice2,ran_choice3]
    pw = random.choice(ran_list)
    print(chr(pw),end="")
