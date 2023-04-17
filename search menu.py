import easygui
def float_checker(text):
    float_ = ""
    while float_ == "":
        try:
            float_ = float(easygui.enterbox(text))
            break
        except ValueError :
            easygui.msgbox("please enter a number")
    return float_
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
search_menu()
print(menus)
