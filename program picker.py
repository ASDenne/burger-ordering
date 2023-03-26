import easygui

options = ["print test","print hello world","exit"]
action = easygui.buttonbox("what are you trying to do?",choices=options)
if action == "print test":
    print("test")
if action == "print hello world":
    print("hello world")


