#1.In Python, you can reuse the function as many times as you want. You can also scale the function and data easily.
#In Excel, you can easily see all of the visualizations and data in one place, which can be helpful for analysis and decision-making.
#2.You could use an append function to add new data, like sales transactions to a composite log.
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
total=.0
totalrevenue=.0
with open('data/sales.csv', 'r') as file:
    reader = csv.reader(file)
    header=next(reader)
    for row in reader:
        item=row[0]
        quantity=int(row[2])
        price=float(row[1])
        total=quantity*price
        totalrevenue+=total
        print(f"Item: {item}, Quantity: {quantity}, Price: {price}, Total: ${total:,.2f}")
print(f"Total Revenue: ${totalrevenue:,.2f}")
print("exercise 5")
import os
input_file = 'data/sales.csv'
output_file = 'data/cleaned.csv'
original_count = 0
written_count = 0
with open(input_file, mode='r', encoding='utf-8', newline='') as infile, \
    open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    original_header = next(reader)
    writer.writerow(['Product', 'Price', 'Qty', 'Total'])
    for row in reader:
        original_count += 1
        product = row[0]
        qty = float(row[1])
        price = float(row[2])
        total = qty * price
        if total>100.0:
            writer.writerow([product, price, qty, total])
            written_count += 1
print(f"Original data rows: {original_count}")
print(f"Rows written (> $100): {written_count}")
print("exercise 6")
totalrevenue=.0
with open('data/sales.csv', 'r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        item_name=row['product']
        qty=int(row['quantity'])
        price=float(row['price'])
        line_total=qty*price
        totalrevenue+=line_total
        print(f"Item: {item_name}, Quantity: {qty}, Price: {price}, Total: ${line_total:,.2f}")
print(f"Total Revenue: ${totalrevenue:,.2f}")
#I perfer DictReader because it allows me to access the data by column names, which makes the code more readable and easier to maintain.
#It is preferble over reader when working with CSV files that have headers, as it eliminates the need to remember the index of each column.
print("exercise 7")
product_totals={}
with open('data/sales.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product=row['product']
        qty=int(row['quantity'])
        price=float(row['price'])
        line_total=qty*price
        product_totals[product]=product_totals.get(product,0)+line_total
print(f"{'Product':<20} {'Total Revenue':>15}")
for product in sorted(product_totals.keys()):
    print(f"{product:<20} ${product_totals[product]:>14,.2f}")
print("exercise 8")
from datetime import datetime
totalrevenue=.0
csv_path='data/sales.csv'
with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        quantity=int(row['quantity'])
        price=float(row['price'])
        line_total=quantity*price
        totalrevenue+=line_total
current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_file='data/run_log.txt'
os.makedirs(os.path.dirname(log_file), exist_ok=True)
log_entry=f"{current_time} - Total Revenue: ${totalrevenue:,.2f}\n"
with open(log_file, 'a') as log:
    log.write(log_entry)
print(f"Log entry added to {log_file}: {log_entry.strip()}")