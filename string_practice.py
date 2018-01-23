def string_to_list(string_char):
    return list(string_char)

def text_repeater(any_thing, amount):
    return ((any_thing + "\n")* amount)

def print_instruction():
    print("1.Print Instructions\n2. Convert String to List\n3.Text Repeater\n4.Pyramid Printing\n5.Exit")

def pattern_print(n, character):
    for i in range (0, n):
        for j in range (0, i + 1):
            print(character, end = "")
        print("\r")

print_instruction()

while True:
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        print_instruction()
    elif choice == 2:
         string_char = input("Enter Any String to Convert into List: ")
         print(list(string_char))
    elif choice == 3:
        any_thing = input("Enter Anything to Repeat: ")
        amount = int(input("Enter Amount: "))
        print(text_repeater(any_thing, amount))
    elif choice == 4:
        n = int(input("Enter Number of rows: "))
        character = input("Enter Character: ")
        pattern_print(n,character)
    elif choice == 5:
        break
    else:
        print("It's Not a Valid Input")
