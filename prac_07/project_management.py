"""
Project Management Program - Client code
Estimated work duration for both class & client code: 3 hours
Current time: 6:31 a.m.
"""

import datetime
from operator import attrgetter

from prac_07.project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
INDEX_DATE = -4
INDEX_PRIORITY = -3
INDEX_COST = -2
INDEX_COMPLETION = -1
MAXIMUM_PERCENTAGE = 100


def main():
    """Load and save project details, use project objects."""
    print(f"Welcome to Pythonic Project Management")
    filename = "projects.txt"
    projects = load_projects(filename)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            pass
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
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
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def display_projects(projects):
    """Display all projects sorted by completion and priority."""
    projects = sorted(projects)
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


def filter_projects(projects):
    """Filter projects by date based on user input."""
    date_string = input("Show projects that start after date (d/m/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    projects.sort(key=attrgetter("date"))
    for project in projects:
        if project.date >= date:
            print(project)


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    project = Project(name, date, priority, cost, completion)
    projects.append(project)


def update_project(projects):
    """Modify completion percentage, priority of a project."""
    for i, project in enumerate(projects):
        print(i, project)
    project_chosen_number = int(input("Project choice: "))
    project_chosen = projects[project_chosen_number]
    print(project_chosen)
    project_chosen.completion = int(input("New Percentage: "))
    project_chosen.priority = int(input("New Priority: "))


main()
