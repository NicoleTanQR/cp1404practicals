"""Modify Existing GUI Program - Class"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Display greeting based on input, clear input and greeting."""

    def build(self):
        """Set up and return the main widget."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle pressing greet button."""
        # print('greet')
        print("test")
        # self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Reset both text field and output label to blank."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
