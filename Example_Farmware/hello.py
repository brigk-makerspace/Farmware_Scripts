#!/usr/bin/env python

'''Hello Farmware

A simple Farmware example that tells FarmBot to log a new message.
'''

from farmware_tools import device

device.log(message='Hello Farmware!', message_type='success')

#plants = app.get_plants()

new_plant = device.add_plant(x=100, y=200)


