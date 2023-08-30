# Step 1: Open the file with the correct encoding
file_path = 'DATAGUJARAT.txt'
emails_list = []

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # Step 2: Read the contents of the file
        file_contents = file.read()

        # Step 3: Find and add all the emails to the list
        import re
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails_list = re.findall(email_pattern, file_contents)

except FileNotFoundError:
    print(f"File not found: {file_path}")
except IOError as e:
    print(f"Error reading the file: {e}")

# Print the list of emails
print(emails_list)

#make txt file
file_name="list.txt"

with open(file_name, "w") as file:
    for name in emails_list:
        file.write((f'{name} \n' ))
    
