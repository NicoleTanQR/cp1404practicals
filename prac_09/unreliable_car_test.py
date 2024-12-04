"""Test UnreliableCar"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar class."""
    my_unreliable_car = UnreliableCar("Prius 1", 100, 60.5)
    my_unreliable_car.drive(40)
    print(my_unreliable_car)


main()
