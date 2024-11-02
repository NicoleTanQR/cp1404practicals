"""
Guitars! - Class
Estimated work duration: 30 min
Current time: 3:27 a.m.
Actual work duration: 35 min (before testing)
"""
CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display data for a guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the guitar is in years."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Return True or False based on age."""
        return self.get_age() >= VINTAGE_AGE
