import csv
with open('sample_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Name', 'Age', 'Department'])
    writer.writerow([1, 'Alice', 22, 'Computer Science'])
    writer.writerow([2, 'Bob', 23, 'Mechanical'])
    writer.writerow([3, 'Charlie', 21, 'Electrical'])

# Display the contents of the CSV file
with open('sample_data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
