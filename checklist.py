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
        print("{} {}".format(index, list_item))
        index += 1


def mark_completed(index):
    update(index, u"\u221A"+read(index))


def select(function_code):

    if function_code.upper() == "C":
        input_item = user_input("Input item:")
        create(input_item)
    elif function_code.upper() == "HELP":
        print("\nPress:\nC to add to list\nR to read from list\nP to display list\nD to remove an item by index\nRm to remove an item by name\nQ to quit\n")
    elif function_code.upper() == "R":
        item_index = int(user_input("Index Number?"))
        print(read(item_index))
    elif function_code.upper() == "P":
        list_all_items()
    elif function_code.upper() == "Q":
        return False
    elif function_code.upper() == "D":
        item_index = int(user_input("Index Number?"))
        destroy(item_index)
    elif function_code.upper() == "RM":
        input_item = user_input("Input item to remove:")
        if input_item in checklist:
            checklist.remove(input_item)
        else:
            print("Item not found in list. Check spelling and capitalization\n")
    else:
        print("Unknown Option")
    return True


def user_input(prompt):
    user_input = input(prompt)
    return user_input


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
