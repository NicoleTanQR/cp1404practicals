"""
Project Management Program - Class
Estimated work duration for both class & client code: 3 hours
Current time: 6:31 a.m.
Actual work duration for both class & client code: ~12 hours
"""

import datetime

MAXIMUM_PERCENTAGE = 100


class Project:
    """Represent a Project object."""

    def __init__(self, name="", date="", priority=0, cost=0.0, completion=0):
        """Initialise a Project instance."""
        self.name = name
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Display data for a project."""
        return (f"{self.name}, start: {self.date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost:.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Sort projects by priority with less than."""
        return self.priority < other.priority

    def is_incomplete(self):
        """Return True or False based on completion."""
        return self.completion < MAXIMUM_PERCENTAGE
