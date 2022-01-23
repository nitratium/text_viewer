import os

content_displayed = "There is no message."

def content_switcher():
    with open(f"{os.getcwd()}/web_service/message.txt", mode='r', encoding='utf-8') as f:
        content_displayed = f.read()

        if content_displayed == "":
            content_displayed == "There is no message."

        f.close()
