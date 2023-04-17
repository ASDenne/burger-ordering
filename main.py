import easygui
def format_menu(menu):
    menu_text = f"take away menu\n" \
                "\n\n" \
                "items\n\n"
    for combo_name, combo_elements in menu.items():
        combo_menu = ""
        combo_cost = 0
        for item_name, item_price in combo_elements.items():
            combo_menu += f"    {item_name} -${item_price}-\n"
            combo_cost += item_price
        menu_text += f"{combo_name} -${round(combo_cost,4)}-\n\n{combo_menu}\n\n"
    return menu_text
def float_checker(text):
    float_ = ""
    while float_ == "":
        try:
            float_ = float(easygui.enterbox(text))
            break
        except ValueError :
            easygui.msgbox("please enter a number")
    return float_
def add_combo():
    combo_name = easygui.enterbox("what do you want to call your combo?")
    combo_size = easygui.integerbox("how many item's in combo")
    combo = {}
    for i in range(0,combo_size):
        item_name = easygui.enterbox(f"what is item number {i+1}?")
        item_price = float_checker(f"how much does {item_name} cost?")
        combo[item_name] = item_price
    menus[combo_name] = combo
    print(menus)
def print_whole_menu():
    easygui.msgbox(format_menu(menus))
def search_menu():
    search = easygui.enterbox("please enter combo name")
    if search in menus:
        combo_menu = ""
        combo_cost = 0
        for item_name, item_price in menus[search].items():
            combo_menu += f"    {item_name} -${item_price}-\n"
            combo_cost += item_price
        while easygui.buttonbox(f"Is this correct? \n{search} -${round(combo_cost,4)}-\n\n{combo_menu}\n\n",choices=["Yes","No"]) == "No":
            combo_items = []
            for item, combo in menus[search].items():
                combo_items.append(item)
            fix = easygui.buttonbox("what's priced wrong?",choices=combo_items)
            right = float_checker("what should it cost?")
            menus[search][fix] = right
            combo_menu = ""
            combo_cost = 0
            for item_name, item_price in menus[search].items():
                combo_menu += f"    {item_name} -${item_price}-\n"
                combo_cost += item_price
    else:
        search_menu()

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
}
options = ["print whole menu","add_combo","search menu","exit"]
action_defs = [print_whole_menu, add_combo, search_menu, exit]
action = easygui.buttonbox("what are you trying to do?",choices=options)
for i in range(0,len(options)):
    if action == options[i]:
        action_defs[i]()
