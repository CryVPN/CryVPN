from kivy.app import App
from kivy.uix.label import Label


class CryVPNApp(App):
    def build(self):
        return Label(text="CryVPN", halign="center")


CryVPNApp().run()