#!/usr/bin/env python

import time, requests

from PIL import ImageFont

from luma.core.interface.serial import spi
from luma.core.virtual import viewport
from luma.core.render import canvas
from luma.oled.device import sh1106

def make_font(name, size):
    return ImageFont.truetype(name, size)

content_displayed = "There is no message."

font = make_font("/home/pi/Desktop/code2000.ttf", 16)

while True:
    requested_text = requests.get('ENTER URL HERE')
    content_displayed = requested_text.text

    if content_displayed == "":
        content_displayed == "There is no message."

    serial = spi(device=0, port=0)
    device = sh1106(serial)

    with canvas(device) as draw:
        w,h = draw.textsize(content_displayed, font)

    virtual = viewport(device, width=max(device.width, w + device.width + device.width), height=max(h, device.height))

    with canvas(virtual) as draw:
        draw.text((device.width, 24), content_displayed, font=font, fill="white")

    x = 0
    while x < device.width + w:
        virtual.set_position((x, 0))
        x += 1
        time.sleep(0.01)
