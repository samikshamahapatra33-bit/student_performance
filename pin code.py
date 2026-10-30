import re

text = input("Enter the text: ")

# Regular expression to identify 6-digit Indian PIN codes
pattern = r'\b[1-9][0-9]{5}\b'

# Extract PIN codes
pin_codes = re.findall(pattern, text)

print("Extracted PIN Codes:", pin_codes)