checklist = list()


def create(item):
    checklist.append(item)


def read(index):
    return checklist[index]


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, color_code(list_item)))
        index += 1


def mark_completed(index):
    update(index, u"\u221A"+read(index))


def select(function_code):

    if function_code.upper() == "C":
        input_item = user_input("Input item: ")
        create(input_item)
    elif function_code.upper() == "HELP":
        print("\nPress:\nC to add to list\nR to read from list\nP to display list\nU to update an item by index\nD to remove an item by index\nRm to remove an item by name\nQ to quit\n")
    elif function_code.upper() == "R":
        item_index = int(user_input("Index number: "))
        print(color_code(read(item_index)))
    elif function_code.upper() == "P":
        list_all_items()
    elif function_code.upper() == "U":
        input_index = int(user_input("Index number: "))
        input_item = user_input("Input new item: ")
        update(input_index,input_item)
    elif function_code.upper() == "Q":
        return False
    elif function_code.upper() == "D":
        item_index = int(user_input("Index number: "))
        destroy(item_index)
    elif function_code.upper() == "RM":
        input_item = user_input("Input item to remove: ")
        if input_item in checklist:
            checklist.remove(input_item)
        else:
            print("Item not found in list. Check spelling and capitalization.\n")
    else:
        print("Unknown Option")
    return True


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def color_code(item):
    print_item = str(item).upper()
    if "RED" in print_item:
        return "\033[31m{}\033[00m".format(item)
    elif "ORANGE" in print_item:
        return "\033[91m{}\033[00m".format(item)
    elif "YELLOW" in print_item:
        return "\033[93m{}\033[00m".format(item)
    elif "GREEN" in print_item:
        return "\033[32m{}\033[00m".format(item)
    elif "BLUE" in print_item:
        return "\033[34m{}\033[00m".format(item)
    elif "PURPLE" in print_item:
        return "\033[35m{}\033[00m".format(item)
    elif "RAINBOW" in print_item:
        return "\033[35m{}\033[00m".format(item)
    else:
        return item


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()

    mark_completed(0)

    list_all_items()

    select("C")
    list_all_items()
    select("R")
    list_all_items()


running = True
while running:
    selection = user_input("Type HELP to display commands\n")

    running = select(selection)
