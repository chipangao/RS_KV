# import smbus2
# import time
# bus = smbus2.SMBus(1)

# addr = 0x0d
# fan_reg = 0x08
# state = 0

# while True:
#     if state == 0:
#         print(0)
#         bus.write_byte_data(addr,fan_reg,0x00)
#         time.sleep(2)
#     elif state ==1:
#         print(1)
#         bus.write_byte_data(addr,fan_reg,0x01)
#         time.sleep(2)
        
# state = (state +1) %2 

import smbus2
import time
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

bus = smbus2.SMBus(1)
addr = 0x0d
fan_reg = 0x08
state = 0
class MyLayout(Widget):
    
    def Add(self):
        print('Add')
        bus.write_byte_data(addr,fan_reg,0x00)
    def Subtract(self):
        bus.write_byte_data(addr,fan_reg,0x01)
        print('Subtract')

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()