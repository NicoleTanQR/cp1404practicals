"""Taxi Simulator"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Let user choose and drive taxi, display costs."""
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
    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Let user choose from list of available taxis."""
    print("Taxis available:")
    display_taxis(taxis)
    taxi_number = int(input("Choose taxi: "))
    try:
        taxi = taxis[taxi_number]
        return taxi
    except IndexError:
        print("Invalid taxi choice")


def display_taxis(taxis):
    """Display taxis stored."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def handle_trip(taxi, total_cost):
    """Handle one taxi trip."""
    if taxi:
        taxi.start_fare()
        distance = float(input("Drive how far? "))
        taxi.drive(distance)
        trip_cost = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
        total_cost += trip_cost
    else:
        print("You need to choose a taxi before you can drive")
    return total_cost


main()
