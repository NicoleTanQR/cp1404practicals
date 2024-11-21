"""UnreliableCar class"""

from random import uniform

from prac_09.car import Car

MINIMUM_NUMBER = 0
MAXIMUM_NUMBER = 100


class UnreliableCar(Car):
    """Specialised version of a Car with reliability aspect."""

    def __init__(self, name, fuel, reliability: float):
        """Initialise an UnreliableCar instance, based on Car class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like Car if random number less than reliability."""
        if uniform(MINIMUM_NUMBER, MAXIMUM_NUMBER) < self.reliability:
            super().drive(distance)
