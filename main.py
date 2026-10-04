from kivy.app import App
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        return Label(text='JARVIS by AREEB - FINAL', font_size='30sp')
MyApp().run()
