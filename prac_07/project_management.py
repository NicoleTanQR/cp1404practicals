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
INDEX_DATE = -4
INDEX_PRIORITY = -3
INDEX_COST = -2
INDEX_COMPLETION = -1
MAXIMUM_PERCENTAGE = 100


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
            display_projects(projects)
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


def load_projects(filename):
    """Load projects from filename."""
    projects = []
    in_file = open(filename)
    in_file.readline()
    for line in in_file:
        parts = line.strip().split()
        name = " ".join(parts[:INDEX_DATE])
        date = parts[INDEX_DATE]
        priority = int(parts[INDEX_PRIORITY])
        cost = float(parts[INDEX_COST])
        completion = int(parts[INDEX_COMPLETION])
        project = Project(name, date, priority, cost, completion)
        projects.append(project)
    in_file.close()
    return projects


def display_projects(projects):
    """Display all projects sorted by completion and priority."""
    projects.sort()
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.completion < MAXIMUM_PERCENTAGE:
            incomplete_projects.append(project)
        else:
            completed_projects.append(project)
    print_group("Incomplete", incomplete_projects)
    print_group("Complete", completed_projects)


def print_group(group_string, projects):
    """Print projects of the same group."""
    print(f"{group_string} projects:")
    for project in projects:
        print(f"  {project}")


main()
