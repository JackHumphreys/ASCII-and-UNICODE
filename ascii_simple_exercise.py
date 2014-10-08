#ASCII simple exercise

choice = int(input("Type 1 for ASCII to text or type 2 for text to ASCII: "))

if choice == 1:
    myint = int(input("Please enter one ASCII code: "))
    print("Your text character equivalent is: {0}".format(chr(myint)))

elif choice == 2:
    mychar = input("Please enter one text character: ")
    print("Your ASCII code equivalent is: {0}".format(ord(mychar)))
