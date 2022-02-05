import getpass
# importing getpass module

pin = "123pin"
# pin is the password

pin_input = getpass.getpass(prompt='Enter your pin: ')
# pin_input is the pin inputted from the user

counts = 3
# this counts the number of attempts, max attempts established as 3

# if pin_input does not match pin, the password is wrong and the user has 2 remaining attempts to enter password
while pin_input != pin:
    counts -= 1
    if counts == 0:
        print("Number of attempts has been exceeded. Account has been locked")
        break
    #     break ends the loop when number of attempts has exceeded 3
    print("Password is incorrect,", counts, "attempts remaining")
    pin_input = getpass.getpass(prompt='Enter your pin: ')
    # when the password is wrong, a message appears prompting user to input password again

if pin_input == pin:
    print("You're in!")
#     if pin_input matches pin, password is correct