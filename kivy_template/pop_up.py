from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class Pop_up(BoxLayout):
    counter = NumericProperty(0)

    def Counter_function(self):
        self.counter += 1
        self.ids.lbl.text = "{}".format(self.counter)

    def First_thread(self):
        self.counter += 1
        self.ids.lbl.text = "{}".format(self.counter)

class PopUp(Popup):
    pass

class MyApp(App):
    def build(self):
        self.load_kv('pop_up.kv')
        return Pop_up() 

if __name__ == "__main__":
    app = MyApp()
    app.run()