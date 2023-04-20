import easygui


def format_menu(menu):
    menu_text = f"take away menu\n" \
                "\n\n" \
                "items\n\n"  # starts writen menu with title
    for combo_name, combo_elements in menu.items():
        combo_menu = ""  # starts writen combo
        combo_cost = 0  # sets combo cost to 0
        for item_name, item_price in combo_elements.items():
            combo_menu += f"    {item_name} -${item_price}-\n"  # adds an item to the  writen combo
            combo_cost += item_price  # adds the cost of the item to the writen cost
        menu_text += f"{combo_name} -${round(combo_cost,4)}-\n\n{combo_menu}\n\n"  # add info about the combo to the writen menu
    return menu_text


def float_checker(text):
    float_ = ""
    while float_ == "":  # continues till got float
        try:
            float_ = float(easygui.enterbox(text))  # trying to get a float
            break
        except ValueError:
            easygui.msgbox("please enter a number")  # ask again if fails
    return float_


def add_combo():
    combo_name = easygui.enterbox("what do you want to call your combo?")  # get combo name
    combo_size = easygui.integerbox("how many item's in combo")  # get how big it is
    combo = {}
    for i_1 in range(0, combo_size):
        item_name = easygui.enterbox(f"what is item number {i_1+1}?")  # getting a item
        item_price = float_checker(f"how much does {item_name} cost?")  # getting its price
        combo[item_name] = item_price  # adding them item to the combo
    menus[combo_name] = combo  # adding the combo to the menu


def print_whole_menu():
    easygui.msgbox(format_menu(menus))  # printing writen menu


def search_menu():
    search = easygui.enterbox("please enter combo name")  # finding out what they're after
    if search in menus:  # if it's found
        combo_menu = ""  # print the combo ,next 5 lines
        combo_cost = 0
        for item_name, item_price in menus[search].items():
            combo_menu += f"    {item_name} -${item_price}-\n"
            combo_cost += item_price
        while easygui.buttonbox(f"Is this correct? \n{search} -${round(combo_cost,4)}-\n\n{combo_menu}\n\n", choices=["Yes", "No"]) == "No":  # continue while combo has a mistake in pricing
            combo_items = []
            for item, combo in menus[search].items():
                combo_items.append(item)  # listing combo items
            fix = easygui.buttonbox("what's priced wrong?", choices=combo_items)  # asking where the mistake is
            right = float_checker("what should it cost?")  # asking how to fix it
            menus[search][fix] = right  # fixing it
            combo_menu = ""  # printing menu again
            combo_cost = 0
            for item_name, item_price in menus[search].items():
                combo_menu += f"    {item_name} -${item_price}-\n"
                combo_cost += item_price
    else:  # if it's not found
        search_menu()  # restart search menu


def delete():
    target = easygui.enterbox("what input do you want to delete?")  # getting what do you want removed
    if target in menus:  # if it's there
        menus.pop(target)  # delete it
        easygui.msgbox(f"{target} deleted")  # tell them you have
    else:  # otherwise
        easygui.msgbox(f"{target} not found could not delete")  # tell them you can't find it and return to menu


menus = {
    "value": {
        "beef burger": 5.69,
        "fries": 1.00,
        "fizzy drink": 1.00
    },
    "cheezy": {
        "cheeseburger": 6.69,
        "fries": 1.00,
        "fizzy drink": 1.00
    },
    "super": {
        "cheeseburger": 6.69,
        "large fries": 2.00,
        "smoothie": 2.00
    }
}  # set's up menu
options = ["print whole menu", "add_combo", "search menu", "delete menu item", "exit"]  # buttons
action_defs = [print_whole_menu, add_combo, search_menu, delete, exit]  # functions connected to above buttons
action = easygui.buttonbox("what are you trying to do?", choices=options)  # ask what action they want to do
for i in range(0, len(options)):
    if action == options[i]:  # checks if action chosen
        action_defs[i]()  # preforms action
