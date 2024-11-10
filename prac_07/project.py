"""
Project Management Program - Class
Estimated work duration for both class & client code: 3 hours
Current time: 6:31 a.m.
"""


class Project:
    """Represent a Project object."""

    def __init__(self, name="", date="", priority=0, cost=0.0, completion=0):
        """Initialise a Project instance."""
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Display data for a project."""
        return (f"{self.name}, start: {self.date}, priority {self.priority}, "
                f"estimate: ${self.cost:.2f}, completion: {self.completion}%")

    def __lt__(self, other):
        """Sort projects by priority with less than."""
        return self.priority < other.priority

