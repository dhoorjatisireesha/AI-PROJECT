import csv

new_data = [
    ["Smartwatch", 200, 30],
    ["Headphones", 50, 40]
]

with open("data
          .csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_data)

print("New data added successfully!")
