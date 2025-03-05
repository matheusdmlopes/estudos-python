from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
import random
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]


class MainApp(App):
    def build(self):
        button = Button(
            text="Hello from Kivy",
            size_hint=(0.5, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        button.bind(on_press=self.on_press_button)
        return button

    def on_press_button(self, instance):
        print("Button pressed")


if __name__ == "__main__":
    MainApp().run()
