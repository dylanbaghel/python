list = []

def add_item(name):
    list.append(name)

def remove_item(name):
    list.remove(name)

def print_list():
    print(list)
def print_inst():
    print("1. print Instruction\n2. Add Item\n3. Remove Item\n4.Quit\n5.Print List")

print("1. print Instruction\n2. Add Item\n3. Remove Item\n4.Quit\n5.Print List")

while True:
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        print_inst()
        continue
    elif choice == 2:
        new_name = input("Enter a Itme to add: ")
        add_item(new_name)
        print(new_name, " is added to the list")
    elif choice == 3:
        del_name = input("Enter a Item to remove: ")
        old_name = del_name
        remove_item(del_name)
        print(old_name, " is deleted")
    elif choice == 4:
        break
    elif choice == 5:
        print_list()
