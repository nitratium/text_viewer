#!/usr/bin/env python

import os
import time

from luma.core.interface.serial import spi
from luma.core.virtual import viewport
from luma.core.render import canvas
from luma.oled.device import sh1106

content_displayed = "There is no message."

while True:
    with open(f"{os.getcwd()}/web_service/message.txt", mode='r', encoding='utf-8') as file:
        content_displayed = file.read()

        if content_displayed == "":
            content_displayed == "There is no message."

    serial = spi(device=0, port=0)
    device = sh1106(serial)

    with canvas(device) as draw:
        w,h = draw.textsize(content_displayed)

    virtual = viewport(device, width=max(device.width, w + device.width + device.width), height=max(h, device.height))

    with canvas(virtual) as draw:
        draw.text((device.width, 0), content_displayed, fill="white")

    x = 0
    while x < device.width + w:
        virtual.set_position((x, 0))
        x += 1
        time.sleep(0.01)
