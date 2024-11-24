"""Taxi Simulator"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Drive taxi based on input and display costs."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_cost = 0.0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            total_cost = handle_trip(current_taxi, total_cost)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    pass


def choose_taxi(taxis):
    """Let user choose from list of available taxis."""
    print("Taxis available:")
    display_taxis(taxis)
    taxi_number = int(input("Choose taxi: "))
    taxi = taxis[taxi_number]
    return taxi


def display_taxis(taxis):
    """Display taxis stored."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def handle_trip(taxi, total_cost):
    """Handle one taxi trip."""
    distance = int(input("Drive how far? "))
    taxi.drive(distance)
    trip_cost = taxi.get_fare()
    print(f"Your {taxi.name} trip will cost you ${trip_cost:.2f}")
    total_cost += trip_cost
    return total_cost


main()
