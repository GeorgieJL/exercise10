import getpass

pin = "123fin"

pin_input = getpass.getpass(prompt='Enter your pin: ')
# attempt = input("Enter your pin: ")

# counts
a = 0
# inputted_pin
while pin_input != pin:
    a += 1
    if a > 2:
        print("Pin has been entered incorrectly", a, "times. Account is locked")
        break
    print("Attempt no.", a)
    pin_input = getpass.getpass(prompt='Enter your pin: ')
    # attempt = input("Enter your pin: ")

if pin_input == pin:
    print("You're in!")




# a = 1
# while attempt != pin:
#   print("Your password is incorrect")
#   a=a+1
#
# else:
#     print("Password correct")
