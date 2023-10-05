import csv

flights_file = open('flights.csv')

csv_reader = csv.reader(flights_file, delimiter=',')

for row in csv_reader:
    print(row[0], row[10])

