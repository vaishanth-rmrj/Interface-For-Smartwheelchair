from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.utils import get_color_from_hex

kv = Builder.load_file("assets/interface.kv")

# colors used
#  dark indigo - rgba(63, 81, 181, 1)

class StartScreen(Screen):
    pass
    
class ControlScreen(Screen):
    pass

class InterfaceScreenManager(ScreenManager):
    pass


class SmartWheelchairInterfaceApp(MDApp):

    def build(self):       
        
        return InterfaceScreenManager()

if __name__ == "__main__":
    SmartWheelchairInterfaceApp().run()