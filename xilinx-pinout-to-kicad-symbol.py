import pandas as pd

pd.read_table("xcku035ffva1156pkg.txt", header=3, skipfooter=3)

# import re

# # Function to parse the file and group pins by Bank
# def parse_and_group_by_bank(file_path):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()

#     # Extract the device/package name from the first line
#     device_name = lines[0].split()[0]

#     # Skip the header lines and start parsing from the pin information
#     pin_lines = lines[3:-1]  # Exclude the footer line

#     # Regular expression to match the pin information, focusing on the Bank
#     pin_regex = r'^(\S+)\s+(\S+)(?:\s+\S+){2}\s+(\S+)'

#     # Parsing each pin line and grouping by Bank
#     pins_by_bank = {}
#     for line in pin_lines:
#         match = re.match(pin_regex, line)
#         if match:
#             pin_number, pin_name, bank = match.groups()
#             if bank not in pins_by_bank:
#                 pins_by_bank[bank] = []
#             pins_by_bank[bank].append((pin_number, pin_name))

#     return device_name, pins_by_bank

# # Function to create a nested KiCad symbol with pins grouped by Bank
# def create_nested_kicad_symbol(device_name, pins_by_bank):
#     symbol = f'(symbol "{device_name}"\n'
#     symbol += '  (in_bom yes)\n'
#     symbol += '  (on_board yes)\n'

#     # Adding symbol properties (placeholders)
#     symbol_properties = [
#         '(property "Reference" "U" (id 0) (at 0 0 0) hide)',
#         '(property "Value" "Device_Value" (id 1) (at 0 0 0) hide)',
#         '(property "Footprint" "" (id 2) (at 0 0 0) hide)',
#         '(property "Datasheet" "" (id 3) (at 0 0 0) hide)'
#     ]
#     for prop in symbol_properties:
#         symbol += f'  {prop}\n'

#     # Graphic items (placeholders)
#     graphic_items = [
#         '(rectangle (start 0 0) (end 10 10) (stroke (width 0.1)))'  # Example rectangle
#     ]
#     for item in graphic_items:
#         symbol += f'  {item}\n'

#     # Adding nested symbols for each bank
#     for bank, pins in pins_by_bank.items():
#         symbol += f'  (symbol "{bank}"\n'
#         for pin_number, pin_name in pins:
#             symbol += f'    (pin standard {pin_number} "{pin_name}")\n'
#         symbol += '  )\n'

#     # End of the symbol definition
#     symbol += ')'

#     return symbol

# # Main function to parse the file and create the KiCad symbol
# def main(file_path):
#     device_name, pins_by_bank = parse_and_group_by_bank(file_path)
#     nested_kicad_symbol = create_nested_kicad_symbol(device_name, pins_by_bank)
#     return nested_kicad_symbol

# # Usage example (you can replace 'file_path' with your file's path)
# file_path = 'your_file_path_here.txt'
# nested_kicad_symbol = main(file_path)
# print(nested_kicad_symbol)
