#1.
#2.
print("exercise 2")
import csv
with open('data/sales.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
print("exercise 3")
with open('data/sales.csv', 'r') as file:
    reader = csv.reader(file)
    header=next(reader)
    print("Header: ", header)
    print("-" * 40)
    print("Data Rows: ")
    for row in reader:
        print(row)
print("exercise 4")