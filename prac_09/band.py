"""Band class"""


class Band:
    """Represent a Band object."""

    def __init__(self, name=""):
        """Initialise a Band instance."""
        self.name = name
        self.members = []

    def __str__(self):
        """Display data for a band."""
        return (f"{self.name} "
                f"({', '.join(str(member) for member in self.members)})")

    def add(self, member):
        """Add a member to the band."""
        self.members.append(member)

    def play(self):
        """Return string on member playing first or no instrument."""
        return "\n".join(member.play() for member in self.members)
