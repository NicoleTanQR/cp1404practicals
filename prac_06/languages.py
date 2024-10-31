"""
Intermediate Exercises - Client code
Estimated work duration: 30 min
Current time: 3 a.m.
Actual work duration: 21 min
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Test programming language class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    programming_languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for programming_language in programming_languages:
        if programming_language.is_dynamic():
            print(programming_language.name)


main()
