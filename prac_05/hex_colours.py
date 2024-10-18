"""Practical 5 - Intermediate Exercises"""

NAME_TO_CODE = {"absolute zero": "#0048ba", "aliceblue": "#f0f8ff",
                "barn red": "#7c0a02", "battleship gray": "#848482",
                "byzantine": "#bd33a4", "gold fusion": "#85754e",
                "gunmetal": "#2a3439", "japanese carmine": "#9d2933",
                "rifle green": "#444c38", "rocket metallic": "#8a7f80"}
print(NAME_TO_CODE)

# Use EAFP approach
# is_valid_input = False
# while not is_valid_input:
#     try:
#         colour_name = input("Enter colour name: ").lower()
#         if colour_name != "":
#             print(NAME_TO_CODE[colour_name])
#         else:
#             is_valid_input = True
#     except KeyError:
#         print("Colour name not found")

# Use get method
colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(NAME_TO_CODE.get(colour_name))
    colour_name = input("Enter a colour name: ").lower()
