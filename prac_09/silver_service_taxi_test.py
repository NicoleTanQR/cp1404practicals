"""Test SilverServiceTaxi"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class."""
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)
    assert hummer.get_fare() == 4.50
    my_silver_service_taxi = SilverServiceTaxi("My Silver Service Taxi", 200,
                                               2)
    my_silver_service_taxi.drive(18)
    print(my_silver_service_taxi)
    # assert my_silver_service_taxi.get_fare() == 48.78
    assert my_silver_service_taxi.get_fare() == 48.80


main()
