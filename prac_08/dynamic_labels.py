"""Dynamic Labels - Class"""

from random import randint

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

FILENAME = "dynamic_labels.kv"
NAMES = ["Alex", "Taylor", "Jordan", "Casey", "Keiko"]
MINIMUM_NUMBER = 0
MAXIMUM_NUMBER = 100


class DynamicLabelsApp(App):
    """Dynamically create a separate label for each name."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_label = {}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file(FILENAME)
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create label for name, adding to dictionary and GUI."""
        for name in NAMES:
            temp_label = Label(
                text=f"{name}_{randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)}")
            self.name_to_label[name] = temp_label
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
