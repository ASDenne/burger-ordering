import easygui
def delete():
    delete = easygui.enterbox("what input do you want to delete?")
    if delete in menus:
        menus.pop(delete)
        easygui.msgbox(f"{delete} deleted")
    else:
        easygui.msgbox(f"{delete} not found could not delete")


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
delete()
print(menus)
