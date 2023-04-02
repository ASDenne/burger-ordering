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
def add_combo():
    combo_name = easygui.enterbox("what do you want to call your combo?")
    combo_size = easygui.integerbox("how many item's in combo")
    combo = {}
    for i in range(0,combo_size):
        item_name = easygui.enterbox(f"what is item number {i}?")
        item_price = float_checker(f"how much does {item_name} cost?")
        combo[item_name] = item_price
    menus[combo_name] = combo
    print(menus)
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
print(menus)
add_combo()


