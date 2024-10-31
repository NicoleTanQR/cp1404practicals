"""
Intermediate Exercises - Class
Estimated work duration: 30 min
Current time: 12:26 a.m.
Actual work duration: 12 min before Client code
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, typing="Dynamic", reflection=False, year=0):
        """Initialise a ProgrammingLanguage instance."""
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True or False based on typing."""
        return self.typing == "Dynamic"
