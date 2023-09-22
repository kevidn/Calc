from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import kivy

# Set Window Size
Window.size = (640, 700)

# Set Minimum Kivy Requirement Version
kivy.require('1.9.0')

# UI Design
class MyRoot(BoxLayout):

    # To create object from class
    def __init__(self):
        super(MyRoot, self).__init__()

    # A method that accepts two arguments
    def calc_symbol(self, symbol):
        self.calc_field.text += symbol

    # Method to clear all text
    def clear(self):
        self.calc_field.text = ""

    # Method to get result
    def get_result(self):
        self.calc_field.text = str(eval(self.calc_field.text))

# App Name
class calc(App):

    def build(self):
        return MyRoot()

calc = calc()
calc.run()