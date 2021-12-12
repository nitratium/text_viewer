import os
import time
content_displayed="There is no message."

print(content_displayed)

while True:
    with open(f"{os.getcwd()}/web_service/depo.txt", mode='r', encoding='utf-8') as f:
        content = f.read()
        if (content == ""):
            content == "There is no message."

    if(content==content_displayed):
        f.close()
        time.sleep(5)
        continue

    else:
        content_displayed = content

    print(content_displayed)
    f.close()
    time.sleep(5)
