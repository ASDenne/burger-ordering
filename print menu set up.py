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
print(format_menu(menus))
