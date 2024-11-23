"""Taxi Simulator"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Drive taxi based on input and display costs."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    total_cost = 0.0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            choose_taxi(taxis, total_cost)
        elif choice == "d":
            pass
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    pass


def choose_taxi(taxis, total_cost):
    """Let user choose from list of available taxis."""
    print("Taxis available:")
    display_taxis(taxis)
    taxi_number = int(input("Choose taxi: "))
    taxi = taxis[taxi_number]
    taxi.drive(0)
    trip_cost = taxi.get_fare()
    total_cost += trip_cost


def display_taxis(taxis):
    """Display taxis stored."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
