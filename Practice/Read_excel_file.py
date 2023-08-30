import pandas as pd

#read file
file_path = 'C:/Users/ksmis/Desktop/Python/Practice/demo.xls'
df = pd.read_excel(file_path)
names_list = df['First Name'].tolist()
print(names_list)

#make txt file
file_name="list.txt"

with open(file_name, "w") as file:
    file.write("[")
    for name in names_list:
        file.write((f'"{name}",' ))
    file.write("]")




