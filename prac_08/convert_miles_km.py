"""Miles to Kilometres Converter - Class"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

ONE_MILE_IN_KILOMETRES = 1.60934

class MilesConverterApp(App):
    """Convert miles to kilometres."""
    output_kilometres = StringProperty()

    def build(self):
        """Set up and return the main widget."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, text):
        """Handle pressing convert button."""
        self.output_kilometres = str(float(text) * ONE_MILE_IN_KILOMETRES)

    def handle_increment(self, text, change):
        """Handle pressing up or down button."""
        self.root.ids.input_miles.text = str(float(text) + change)


MilesConverterApp().run()
