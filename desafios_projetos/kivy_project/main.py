from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage


class MainApp(App):
    def build(self):
        label = Label(
            text="Hello from Kivy",
            size_hint=(0.5, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        img = AsyncImage(
            source="https://www.python.org/static/img/python-logo.png",
            size_hint=(1, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        return img


if __name__ == "__main__":
    MainApp().run()
