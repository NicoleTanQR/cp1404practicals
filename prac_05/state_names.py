"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

is_valid_input = False
while not is_valid_input:
    try:
        state_code = input("Enter short state: ").upper()
        if state_code != "":
            print(state_code, "is", CODE_TO_NAME[state_code])
        else:
            is_valid_input = True
    except KeyError:
        print("Invalid short state")

code_width = max((len(state_code) for state_code in CODE_TO_NAME))
for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:{code_width}} is {state_name}")
