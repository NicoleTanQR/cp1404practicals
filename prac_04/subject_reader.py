"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Display data from file using lists."""
    data = load_data()
    print(data)
    display_data_sentences(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


def display_data_sentences(data):
    """Display sentence based on data."""
    for parts in data:
        subject, name, number_of_students = parts
        name_width = max((len(parts[1]) for parts in data))
        number_of_students_width = max((len(str(parts[2])) for parts in data))
        print(f"{subject} is taught by {name:{name_width}} and has "
              f"{number_of_students:{number_of_students_width}} students")


main()
