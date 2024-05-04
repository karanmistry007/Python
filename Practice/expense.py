import re


def extract_values_from_string(text):
    pattern = r": (\d+(,\d+)*)/-"
    matches = re.findall(pattern, text)
    values = [match[0].replace(",", "") for match in matches]
    return values


expense_string = """
Date:  21-04-2024
Dad: 20,000/-
"""

expense_list = extract_values_from_string(expense_string)
total_expense = 0

for item in expense_list:
    total_expense += int(item)

print(total_expense)