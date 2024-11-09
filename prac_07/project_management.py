"""
Project Management Program - Client code
Estimated work duration for both class & client code: 3 hours
Current time: 6:31 a.m.
"""

import datetime

from prac_07.project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

def main():
    """Load and save project details, use project objects."""
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} "
          f"projects from {filename}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    pass


main()
