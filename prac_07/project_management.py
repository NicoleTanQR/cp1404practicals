"""
Project Management Program - Client code
Estimated work duration for both class & client code: 3 hours
Current time: 6:31 a.m.
Actual work duration: ~12 hours
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
            filename = input("Filename: ")
            save_projects(filename, projects)
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
    save_confirmation = input(
        f"Would you like to save to {filename}? ").upper()
    if save_confirmation in "YES":
        save_projects(filename, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from filename."""
    projects = []
    with open(filename) as in_file:
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
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(filename, projects):
    """Overwrite file contents with updated projects."""
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\t"
                       "Completion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t"
                           f"{project.date.strftime('%d/%m/%Y')}\t"
                           f"{project.priority}\t{project.cost}\t"
                           f"{project.completion}\n")


def display_projects(projects):
    """Display all projects sorted by completion and priority."""
    projects = sorted(projects)
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.is_incomplete():
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
    try:
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        projects = sorted(projects, key=attrgetter("date"))
        for project in projects:
            if project.date >= date:
                print(project)
    except ValueError:
        print("Invalid date format")


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    try:
        date = input("Start date (dd/mm/yy): ")
        priority = int(input("Priority: "))
        cost = float(input("Cost estimate: $"))
        completion = int(input("Percent complete: "))
        project = Project(name, date, priority, cost, completion)
        projects.append(project)
    except ValueError:
        print("At least one invalid input")


def update_project(projects):
    """Modify completion percentage, priority of a project."""
    for i, project in enumerate(projects):
        print(i, project)
    project_chosen_number = input("Project choice: ")
    if project_chosen_number != "":
        try:
            project_chosen = projects[int(project_chosen_number)]
            print(project_chosen)
            project_chosen.completion = get_integer("New Percentage: ",
                                                    project_chosen.completion)
            project_chosen.priority = get_integer("New Priority: ",
                                                  project_chosen.priority)
        except ValueError:
            print("Invalid integer")
        except IndexError:
            print("Invalid project number")


def get_integer(prompt, existing_value):
    """Return integer, with blank returning existing value."""
    value_string = input(prompt)
    if value_string == "":
        number = existing_value
    else:
        number = int(value_string)
    return number


main()
