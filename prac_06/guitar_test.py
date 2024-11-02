"""
Guitars! - Testing
Estimated work duration: 30 min
Current time: 12:52 p.m.
Actual work duration: 22 min
"""

from prac_06.guitar import Guitar


def main():
    """Test Guitar class."""
    gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 12345)
    print(f"{gibson_guitar.name} get_age() - Expected 100. "
          f"Got {gibson_guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. "
          f"Got {another_guitar.get_age()}")
    print(f"{gibson_guitar.name} is_vintage() - Expected True. "
          f"Got {gibson_guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. "
          f"Got {another_guitar.is_vintage()}")


main()
