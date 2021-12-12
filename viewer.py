import os
import tkinter

content_displayed = "There is no message."

root = tkinter.Tk()
root.attributes('-fullscreen', True)
root.title("Displayer")

v = tkinter.StringVar()
v.set("There is no message.")

label = tkinter.Label(root, textvariable=v, justify="center", fg="white", height=72, width=274, bg="black", font=("calibri", 64))
label.pack()

def content_switcher():
    with open(f"{os.getcwd()}/web_service/depo.txt", mode='r', encoding='utf-8') as f:
        content_displayed = f.read()

        if content_displayed == "":
            content_displayed == "There is no message."

        f.close()
        v.set(content_displayed)
        root.after(1000, content_switcher)

root.after(0, content_switcher)
root.mainloop()
